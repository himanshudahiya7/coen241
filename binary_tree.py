from mininet.topo import Topo

class BinaryTreeTopo( Topo ):
    "Binary Tree Topology Class."

    def __init__( self ):
        "Create the binary tree topology."

        # Initialize topology
        Topo.__init__( self )

	# Add hosts
	h1 = self.addHost('h1')
	h2 = self.addHost('h2')
	h3 = self.addHost('h3')
	h4 = self.addHost('h4')
	h5 = self.addHost('h5')
	h6 = self.addHost('h6')
	h7 = self.addHost('h7')
	h8 = self.addHost('h8')

	# Add switches
	s1 = self.addSwitch('s1')
	s2 = self.addSwitch('s2')
	s3 = self.addSwitch('s3')
	s4 = self.addSwitch('s4')
	s5 = self.addSwitch('s5')
	s6 = self.addSwitch('s6')
	s7 = self.addSwitch('s7')

	# Add links
	self.addlink(h1,s3)
	self.addlink(h2,s3)
	self.addlink(h3,s4)
	self.addlink(h4,s4)
	self.addlink(h5,s6)
	self.addlink(h6,s6)
	self.addlink(h7,s7)
	self.addlink(h8,s7)
	self.addlink(s3,s2)
	self.addlink(s4,s2)
	self.addlink(s6,s5)
	self.addlink(s7,s5)
	self.addlink(s2,s1)
	self.addlink(s5,s1)
	

topos = { 'binary_tree': ( lambda: BinaryTreeTopo() ) }
