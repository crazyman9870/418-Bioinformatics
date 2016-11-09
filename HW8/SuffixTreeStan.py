import sys
from collections import OrderedDict

oo = sys.maxint / 2

class Node:
    def __init__( self, start, end ):
        self.start = start
        self.end = end
        self.edges = OrderedDict()
        self.link = 0

    def edge_length( self, position ):
        return min( self.end, position + 1 ) - self.start

    def get_edges( self ):
        return self.edges

    def set_start( self, start ):
        self.start = start

    def get_start( self ):
        return self.start

    def get_end( self ):
        return self.end

    def set_end( self, end ):
        self.end = end

    def put_edge( self, key, val ):
        self.edges[ key ] = val

    def set_link( self, node ):
        self.link = node

    def get_link( self ):
        return self.link

    def get_edge( self, key ):
        #print "*******************key:", key
        if key in self.edges:
            return self.edges[ key ]
        else:
            return None

    def str_val( self ):
        string = "start: " + str( self.start ) + " end: " + str( self.end ) + " edges: " + str( self.edges )
        return string

    def increment_start( self, val ):
        #print "modifying start to:", (self.start + val)
        self.start += val

counter = 0

class SuffixTree:
    def __init__( self, text ):
        t_len = len( text )
        self.cur_node = 0
        self.nodes_added = 0
        self.nodes = [ Node( 0, oo ) ] * ( 2 * t_len + 2 )
        self.text = ""
        self.root = self.new_node( -1, -1 )
        self.pos = -1
        self.need_link = 0
        self.r = 0

        self.active_node = self.root
        self.active_length = 0
        self.active_edge = 0

        self.index_text( text )

    def get_root_node( self ):
        return self.nodes[ self.root ]

    def get_triple( self ):
        return self.active_node, self.get_active_edge(), self.active_length, self.r

    def get_triple_str( self, w_str ):
        ret_str = "active node:\t" + str( self.active_node ) + "\n"
        ret_str += "active edge:\t" + str( w_str[ self.active_edge ] ) + "\n"
        ret_str += "active length:\t" + str( self.active_length ) + "\n"
        ret_str += "remainder:\t" + str( self.r )

        return ret_str

    def index_text( self, text ):
        for char in text:
            self.add_char( char )

    def add_char( self, c ):
        self.text += c
        self.pos += 1

        self.need_link = -1
        self.r += 1
        global counter

        while self.r > 0:
            if self.active_length == 0:
                self.active_edge = self.pos

            if self.get_active_edge() not in self.nodes[ self.active_node ].get_edges():
                leaf = self.new_node( self.pos, oo )
                self.nodes[ self.active_node ].put_edge( self.get_active_edge(), leaf )
                self.add_suffix_link( self.active_node )
            else:
                nex = self.nodes[ self.active_node ].get_edge( self.get_active_edge() )
                if self.walk_down( nex ):
                    continue

                if self.text[ self.nodes[ nex ].get_start() + self.active_length ] == c:
                    self.active_length += 1
                    self.add_suffix_link( self.active_node )
                    break

                split = self.new_node( self.nodes[ nex ].get_start(), self.nodes[ nex ].get_start() + self.active_length )

                self.nodes[ self.active_node ].put_edge( self.get_active_edge(), split )

                leaf = self.new_node( self.pos, oo )
                self.nodes[ split ].put_edge( c, leaf)
                self.nodes[ nex ].increment_start( self.active_length )
                self.nodes[ split ].put_edge( self.text[ self.nodes[ nex ].get_start() ], nex )
                self.add_suffix_link( split )

            self.r -= 1

            if self.active_node == self.root and self.active_length > 0:
                self.active_length -= 1
                self.active_edge = self.pos - self.r + 1
            else:
                self.active_node = self.nodes[ self.active_node ].get_link() if self.nodes[ self.active_node ].get_link() > 0 else self.root
            
    def walk_down( self, nex ):
        if self.active_length >= self.nodes[ nex ].edge_length( self.pos ):
            self.active_edge += self.nodes[ nex ].edge_length( self.pos )
            self.active_length -= self.nodes[ nex ].edge_length( self.pos )
            self.active_node = nex
            return True
        return False

    def get_active_edge( self ):
        return self.text[ self.active_edge ]

    def new_node( self, start, end ):
        self.cur_node += 1
        self.nodes[ self.cur_node ] = Node( start, end )
        self.nodes_added += 1
        return self.cur_node

    def add_suffix_link( self, node ):
        if self.need_link > 0:
            self.nodes[ self.need_link ].set_link( node )
        self.need_link = node

    def edge_string( self, node ):
        start = self.nodes[ node ].get_start()
        end = min( self.pos + 1, self.nodes[ node ].get_end() )
        return self.text[ start : end ]

    def print_tree(self ):
        self.print_edges( self.root )

    def get_graphviz_tree( self ):
        stree = "" + "\n"
        stree += "digraph {" + "\n"
        stree += "\trankdir = LR;" + "\n"
        stree += "\tedge [arrowsize=0.4,fontsize=10]" + "\n"
        stree += "\tnode1 [label=\"1\",style=filled,fillcolor=lightgrey,shape=circle,width=.1,height=.1];" + "\n"
        stree += "//------leaves------" + "\n"
        leaves = []
        self.print_gv_leaves( self.root, leaves )
        for leaf in leaves:
            stree += leaf

        stree += "//------internal nodes------" + "\n"
        nodes = []
        self.print_gv_internal_nodes( self.root, nodes )
        for node in nodes:
            stree += node

        stree += "//------edges------" + "\n"
        edges = []
        self.print_gv_edges( self.root, edges )
        for edge in edges:
            stree += edge

        stree += "//------suffix links------" + "\n"
        links = []
        self.print_gv_suffix_links( self.root, links )
        for link in links:
            stree += link

        stree += "}"
        return stree

    def print_edges( self, x ):
        for key, child in self.nodes[ x ].get_edges().iteritems():
            print self.edge_string( child )
            self.print_edges( child )

    def print_gv_internal_nodes( self, x, stree ):
        if x != self.root and len( self.nodes[ x ].get_edges() ) > 0:
            stree.append( "\tnode" + str( x ) + " [label=\"" + str( x ) + "\",style=filled,fillcolor=lightgrey,shape=circle,width=.07,height=.07]" + "\n" )
        for key, child in self.nodes[ x ].get_edges().iteritems():
            self.print_gv_internal_nodes( child, stree )

    def print_gv_suffix_links( self, x, stree ):
        if self.nodes[ x ].get_link() > 0:
            stree.append( "\tnode" + str( x ) + " -> node" + str( self.nodes[ x ].get_link() ) + " [label=\"\",weight=1,style=dotted]" + "\n" )
        for key, child in self.nodes[ x ].get_edges().iteritems():
            self.print_gv_suffix_links( child, stree )

    def print_gv_edges( self, x, stree ):
        max_len = len( self.text )
        for key, child in self.nodes[ x ].get_edges().iteritems():
            start = str( self.nodes[ child ].get_start() )
            end = self.nodes[ child ].get_end()
            if end > max_len:
                end = str( max_len )
            else:
                end = str( end )
            stree.append( "\tnode" + str( x ) + " -> node" + str( child ) + " [label=\"" + self.edge_string( child ) + "\t" + start + ", " + end + "\",weight=3]" + "\n" )
            self.print_gv_edges( child, stree )

    def print_gv_leaves( self, x, stree ):
        if len( self.nodes[ x ].get_edges() ) == 0:
            stree.append( "\tnode" + str( x ) + " [label=\"" + str( x ) + "\",style=filled,fillcolor=lightgrey,shape=circle,width=.07,height=.07]" + "\n" )
        else:
            for key, child in self.nodes[ x ].get_edges().iteritems():
                self.print_gv_leaves( child, stree )

    def tree_to_file( self, name = None ):
        global counter
        if len( str( counter ) ) == 1:
            my_counter = "0" + str( counter )
        else:
            my_counter = str( counter )

        if name is None:
            file_name = "tree." + my_counter + ".dot"
        else:
            file_name = "tree." + my_counter + "." + name + ".dot"
        counter += 1
        with open( file_name, 'w' ) as fh:
            fh.write( tree.get_graphviz_tree() )
        return file_name

    def get_tree_edge( self, cur_node, child_char ):
        return self.nodes[ cur_node.get_edge( child_char ) ]


if __name__ == "__main__":
    text = "somethinglong$"
    suffix_tree = SuffixTree( text )

    #print suffix_tree.get_graphviz_tree()
    root = suffix_tree.get_root_node()
    cur_node = root

    print "ROOOOOOOOOOOOOT ",root
    for edge_char, edge_start in cur_node.get_edges().iteritems():
        edge = suffix_tree.get_tree_edge( cur_node, edge_char )
        edge_idx = cur_node.get_edge( edge_char )
        
        print "edge char:", edge_char, "(", edge_start, ")"
        print "\tchild start:", edge.get_start()
        print "\tchild end:", edge.get_end()
        print "\tchild substring:", suffix_tree.edge_string( edge_idx )
        
