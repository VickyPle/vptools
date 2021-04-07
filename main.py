import nuke

def setup_menu():
    nuke.menu('Nuke').addCommand('VP Tools/Basic Match Grade', create_basic_match_grade_setup)
    nuke.menu('Nuke').addCommand('VP Tools/Basic Script', create_basic_script)
    nuke.menu('Nuke').addCommand('VP Tools/Tidy Nodes', tidyNodes)


def create_basic_match_grade_setup():
    nuke.nodes.BackdropNode(label='Basic Match Grade', note_font_size=20)
    Grade1 = nuke.nodes.Grade(black_clamp=False)
    Grade2 = nuke.nodes.Grade(inputs=[Grade1], black_clamp=False)
    Grade3 = nuke.nodes.Grade(inputs=[Grade2])

def create_basic_script():
    ReadNode = nuke.nodes.Constant(label='Read Node Placeholder', color=1)
    Dot = nuke.nodes.Dot(inputs=[ReadNode])
    nuke.nodes.Write(inputs=[Dot])

def tidyNodes():
    nodes = nuke.selectedNodes()    
    amount = len(nodes)    
    if amount == 0:    
        return 

    allX = sum([n.xpos()+n.screenWidth()/2 for n in nodes])  
    allY = sum([n.ypos()+n.screenHeight()/2 for n in nodes]) 

    centreX = allX / amount
    centreY = allY / amount

    for n in nodes:
        n.setXpos(centreX + ( n.xpos() - centreX) * 1)
        n.setYpos(centreY + ( n.ypos() - centreY) * 1)

    


    
    # selectedNode = nuke.selectedNode()
    # selectedNode['value'].setValue(100)
    # nuke.nodes.Multiply(inputs=[selectedNode])
    # for i in range(100):
    #     nuke.nodes.Multiply(value=i)
    


# nuke.menu('Nuke').addCommand('MyMenu/my tool 1', lambda: nuke.message('yay, it works'))
# nuke.menu('Nuke').addCommand('MyMenu/my tool 2', "nuke.message('yay, it works too')", icon='VP_Logo.png')
# nuke.menu('Nuke').addCommand('MyMenu/my tool 1.5', "nuke.message('yay, it works too')", index=1)
# m.addSeparator()
# nuke.menu('Nuke').addCommand('MyMenu/my tool 3', "nuke.message('yay, it works too')")

