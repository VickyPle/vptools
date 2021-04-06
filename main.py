import nuke

def setup_menu():
    nuke.menu('Nuke').addCommand('VP Tools/Basic Match Grade', create_basic_match_grade_setup)


def create_basic_match_grade_setup():
    nuke.nodes.BackdropNode(label='Basic Match Grade', note_font_size=20)
    Grade1 = nuke.nodes.Grade(black_clamp=False)
    Grade2 = nuke.nodes.Grade(inputs=[Grade1], black_clamp=False)
    Grade3 = nuke.nodes.Grade(inputs=[Grade2])
    
    


    
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

