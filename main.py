import nuke

def setup_menu():
    m = nuke.menu('Viewer')
    VPMenu = m.addMenu('VPTools')
    VPToolbar = nuke.toolbar('VP Menu')
    VPMenu = VPToolbar.addMenu('VP Tools', icon = './vptools/VP_Logo.png')
    VPToolbar.addCommand('VP Tools/tool A', create_awesome_graph)

def create_awesome_graph():
    selectedNode = nuke.selectedNode()
    selectedNode['value'].setValue(100)
    nuke.nodes.Multiply(inputs=[selectedNode])
    # for i in range(100):
    #     nuke.nodes.Multiply(value=i)
    


# nuke.menu('Nuke').addCommand('MyMenu/my tool 1', lambda: nuke.message('yay, it works'))
# nuke.menu('Nuke').addCommand('MyMenu/my tool 2', "nuke.message('yay, it works too')", icon='VP_Logo.png')
# nuke.menu('Nuke').addCommand('MyMenu/my tool 1.5', "nuke.message('yay, it works too')", index=1)
# m.addSeparator()
# nuke.menu('Nuke').addCommand('MyMenu/my tool 3', "nuke.message('yay, it works too')")

