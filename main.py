from __future__ import division
from sympy import *
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from pyperclip import *


x, y, z, t, p, q, a, r, θ, φ, ρ = symbols('x y z t p q a r θ φ ρ')

screen_helper = """
ScreenManager:
    MenuScreen:
    AboutScreen:
    LapCordScreen:
    LapCordCar:
    LapCordCyl:
    LapCordSph:
    LapCordFORM:
    GradCordScreen:
    GradCordCar:
    GradCordCyl:
    GradCordSph:
    GradCordFORM:
    EGcord:
    EGcar:
    EGcyl:
    EGsph:





<MenuScreen>:
    name:'MainMenu'
    Screen:
        MDLabel:
            text: "Which operation would you like to perform?"
            halign:'center'
            pos_hint: {"center_y": 0.7}


            theme_text_color: "Custom"
            text_color: 1, 196/255, 0, 1

        MDRectangleFlatButton:
            text:"Laplacian"
            pos_hint: {'center_x':0.5,'center_y':0.5}
            on_press: root.manager.current = 'LapCordScreen'  

        MDRectangleFlatButton:
            text:"Gradient"
            pos_hint: {'center_x':0.5,'center_y':0.4}
            on_press: root.manager.current = 'GradCordScreen'
        
        MDRectangleFlatButton:
            text:"Calculating E using E = −grad V"
            pos_hint: {'center_x':0.5,'center_y':0.3}
            on_press: root.manager.current = 'EGcord'       
            
             
            
                

        NavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:

                            title: 'Main'
                            md_bg_color: [0, 0, 0, .3]
                            left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                            elevation:5
                            specific_text_color: 1, 196/255, 0, 1
                        Widget:    

            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'


                    Image:
                        source:'resources/UoBeng.png'


                    MDLabel:
                        text: ''
                        size_hint_y: None
                        height: self.texture_size[1]  


                    ScrollView:  
                        MDList:
                            OneLineListItem:
                                text: 'Laplacian'
                                theme_text_color: "Custom"
                                text_color: 1, 196/255, 0, 1
                                on_press: root.manager.current = 'LapCordScreen' 


                            OneLineListItem:
                                text: 'Gradient'
                                theme_text_color: "Custom"
                                text_color: 1, 196/255, 0, 1
                                on_press: root.manager.current = 'GradCordScreen'  
                                
                            OneLineListItem:
                                text: 'Calculating E using E = −grad V'
                                theme_text_color: "Custom"
                                text_color: 1, 196/255, 0, 1
                                on_press: root.manager.current = 'EGcord' 
                                
                                
                                
                                    


                               




                            OneLineListItem:
                                text: 'About'
                                theme_text_color: "Custom"
                                text_color: 1, 196/255, 0, 1
                                on_press: root.manager.current = 'About'  

<LapCordScreen>:
    name:'LapCordScreen'
    
    MDLabel:
        text: 'Laplacian of V can be expressed in Cartesian, cylindrical, and spherical coordinates'
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 1
        halign:'center'
        pos_hint: {'center_y':0.8}
    

    MDRectangleFlatButton:
        text:"Laplacian of V in cartesian coordinates"
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_press: root.manager.current = 'LapCordCar'  

    MDRectangleFlatButton:
        text:"Laplacian of V in cylindrical coordinates"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'LapCordCyl'  

    MDRectangleFlatButton:
        text:"Laplacian of V in spherical coordinates"
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'LapCordSph' 
    
    MDRectangleFlatButton:
        text:"Laplacian formulas"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'LapCordFORM'            


<GradCordScreen>:
    name:'GradCordScreen'
    
    MDLabel:
        text: 'Gradient of V can be expressed in Cartesian, cylindrical, and spherical coordinates'
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 1
        halign:'center'
        pos_hint: {'center_y':0.8}
    
    
    MDRectangleFlatButton:
        text:"Gradient of V in cartesian coordinates"
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_press: root.manager.current = 'GradCordCar'  

    MDRectangleFlatButton:
        text:"Gradient of V in cylindrical coordinates"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'GradCordCyl'  

    MDRectangleFlatButton:
        text:"Gradient of V in spherical coordinates"
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'GradCordSph'
    
    MDRectangleFlatButton:
        text:"Gradient formulas"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'GradCordFORM'                 

<AboutScreen>:
    name:'About'
    Image:
        source:'resources/UoB.PNG'
        
        pos_hint: {'center_x':0.5,'center_y':0.8}
        size: self.texture_size
        size_hint_y: 0.4
        
        
        

    MDLabel:
        text: 'This app was developed by the students of University of Benghazi'
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 1
        halign:'center' 
        pos_hint: {'center_y':0.55}
    
    MDLabel:
        text: 'Mohamed S. Gabriel - Developer'
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 1
        halign:'center' 
        pos_hint: {'center_y':0.43}
        
    MDLabel:
        text: 'Esmaeil Alkhazmi - Developer'
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 1
        halign:'center' 
        pos_hint: {'center_y':0.40} 
        
    MDLabel:
        text: 'Asst. Prof. Asma Alfergani - Quality Coordinator '
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 1
        halign:'center' 
        pos_hint: {'center_y':0.3}        
        
    MDLabel:
        text: 'This app was made by Kivy which is an Open source Python library.' 
        pos_hint: {'center_y':0.18}    
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 1
        halign:'center'      
    MDRectangleFlatButton:
        text:"Main Menu"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'MainMenu'  

<LapCordCar>:
    name:'LapCordCar'

    MDLabel:
        text: 'Laplacian of V in cartesian coordinates'
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 1
        halign:'center'
        pos_hint: {'center_y':0.7} 
    MDRectangleFlatButton:
        text:"Main Menu"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'MainMenu' 

    MDTextField:
        hint_text: "Enter your function here"
        helper_text: "use parameters for best results, ex: 5*(x^2)*sin(x)"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:270
        id:  textfieldLapCordCart   
    MDRectangleFlatButton:
        text:'calculate'
        pos_hint:{'center_x': 0.5, 'center_y': 0.3}
        on_release: app.root.get_screen("LapCordCar").change_variable(textfieldLapCordCart.text)
        
       


<LapCordCyl>:
    name:'LapCordCyl'

    MDLabel:
        text: 'Laplacian of V in cylindrical coordinates'
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 1
        halign:'center'
        pos_hint: {'center_y':0.9}

    MDLabel:
        text: 'for easy input, click on the following to copy the symbol:'
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 1
        halign:'center'
        pos_hint: {'center_y':0.8}
    
        

    MDRoundFlatButton:
        text:'ρ'
        id:  p_text 
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        on_release: app.root.get_screen("LapCordCyl").symbols_p(p_text.text)


    MDRoundFlatButton:
        text:'φ'
        id:  φ_text 
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        on_release: app.root.get_screen("LapCordCyl").symbols_phai(φ_text.text)
    
    
    MDRectangleFlatButton:
        text:"Main Menu"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'MainMenu' 

    MDTextField:
        hint_text: "Enter your function here"
        helper_text: "use parameters for best results, ex: 5*(ρ^2)*sin(φ)"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:270
        id:  textfieldLapCordCyln   
        
    MDRectangleFlatButton:
        text:'calculate'
        pos_hint:{'center_x': 0.5, 'center_y': 0.3}
        on_release: app.root.get_screen("LapCordCyl").change_variable(textfieldLapCordCyln.text)     

<LapCordSph>:
    name:'LapCordSph'

    MDLabel:
        text: 'Laplacian of V in spherical coordinates'
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 1
        halign:'center'
        pos_hint: {'center_y':0.9}

    MDLabel:
        text: 'for easy input, click on the following to copy the symbol:'
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 1
        halign:'center'
        pos_hint: {'center_y':0.8}
    

    MDRectangleFlatButton:
        text:"Main Menu"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'MainMenu' 

    MDTextField:
        hint_text: "Enter your function here"
        helper_text: "use parameters for best results, ex: 5*(r^2)*sin(θ)"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:270
        id:  textfieldLapCordSphr   
        
    MDRectangleFlatButton:
        text:'calculate'
        pos_hint:{'center_x': 0.5, 'center_y': 0.3}
        on_release: app.root.get_screen("LapCordSph").change_variable(textfieldLapCordSphr.text) 
        
    MDRoundFlatButton:
        text:'θ'
        id:  a_text 
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        on_release: app.root.get_screen("LapCordSph").symbols_theta(a_text.text)


    MDRoundFlatButton:
        text:'φ'
        id:  aq_text 
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        on_release: app.root.get_screen("LapCordCyl").symbols_phai(aq_text.text)    
        
<LapCordFORM>:
    name:'LapCordFORM'
    Image:
        source:'resources/LAP.PNG'
    MDRectangleFlatButton:
        text:"Main Menu"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'MainMenu'    
<GradCordFORM>:
    name:'GradCordFORM'
    Image:
        source:'resources/GRAD.PNG'  
    MDRectangleFlatButton:
        text:"Main Menu"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'MainMenu'           

<GradCordCar>:
    name:'GradCordCar'

    MDLabel:
        text: 'Gradient of V in cartesian coordinates'
        halign:'center'
        pos_hint: {"center_y": 0.7}
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 1
    MDRectangleFlatButton:
        text:"Main Menu"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'MainMenu'

    MDTextField:
        hint_text: "Enter your function here"
        helper_text: "use parameters for best results, ex: 5*(x^2)*sin(x)"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:270
        id:  textfieldGradCordCar   
    MDRectangleFlatButton:
        text:'calculate'
        pos_hint:{'center_x': 0.5, 'center_y': 0.3}
        on_release: app.root.get_screen("GradCordCar").change_variable(textfieldGradCordCar.text)

<GradCordCyl>:
    name:'GradCordCyl'

    MDLabel:
        text: 'Gradient of V in cylindrical coordinates'
        halign:'center'
        pos_hint: {"center_y": 0.9}
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 

    MDLabel:
        text: 'for easy input, click on the following to copy the symbol:'
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 1
        halign:'center'
        pos_hint: {'center_y':0.8}
        
        

    MDRoundFlatButton:
        text:'ρ'
        id:  pg_text 
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        on_release: app.root.get_screen("LapCordCyl").symbols_p(pg_text.text)


    MDRoundFlatButton:
        text:'φ'
        id:  aba_text 
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        on_release: app.root.get_screen("LapCordCyl").symbols_phai(aba_text.text)

    MDRectangleFlatButton:
        text:"Main Menu"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'MainMenu'

    MDTextField:
        hint_text: "Enter your function here"
        helper_text: "use parameters for best results, ex: 5*(x^2)*sin(x)"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:270
        id:  textfieldGradCordCyl  
    MDRectangleFlatButton:
        text:'calculate'
        pos_hint:{'center_x': 0.5, 'center_y': 0.3}
        on_release: app.root.get_screen("GradCordCyl").change_variable(textfieldGradCordCyl.text)  

<GradCordSph>: 
    name:'GradCordSph'

    MDLabel:
        text: 'Gradient of V in spherical coordinates'
        halign:'center'
        pos_hint: {"center_y": 0.9}
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 

    MDLabel:
        text: 'for easy input, click on the following to copy the symbol:'
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 1
        halign:'center'
        pos_hint: {'center_y':0.8}

    

    MDRectangleFlatButton:
        text:"Main Menu"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'MainMenu'
        
    MDRoundFlatButton:
        text:'θ'
        id:  aaa_text 
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        on_release: app.root.get_screen("LapCordSph").symbols_theta(aaa_text.text)


    MDRoundFlatButton:
        text:'φ'
        id:  aqaq_text 
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        on_release: app.root.get_screen("LapCordCyl").symbols_phai(aqaq_text.text)    

    MDTextField:
        hint_text: "Enter your function here"
        helper_text: "use parameters for best results, ex: 5*(r^2)*sin(θ)"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:270
        id:  textfieldGradCordSph   
    MDRectangleFlatButton:
        text:'calculate'
        pos_hint:{'center_x': 0.5, 'center_y': 0.3}
        on_release: app.root.get_screen("GradCordSph").change_variable(textfieldGradCordSph.text) 
        
<EGcord>:
    name:'EGcord'
    MDLabel:
        text: 'E can be found by using E = −grad V in Cartesian,cylindrical and spherical coordinates'
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 1
        halign:'center'
        pos_hint: {'center_y':0.8}
    

    MDRectangleFlatButton:
        text:"E = −grad V using cartesian coordinates"
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_press: root.manager.current = 'EGcar'  

    MDRectangleFlatButton:
        text:"E = −grad V using cylindrical coordinates"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'EGcyl'  

    MDRectangleFlatButton:
        text:"E = −grad V using spherical coordinates"
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'EGsph' 
    
    MDRectangleFlatButton:
        text:"Gradient formulas"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'GradCordFORM'            


<EGcar>:
    name:'EGcar'
    MDLabel:
        text: 'E = −grad V using cylindrical coordinates'
        halign:'center'
        pos_hint: {"center_y": 0.7}
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 1
    MDRectangleFlatButton:
        text:"Main Menu"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'MainMenu'

    MDTextField:
        hint_text: "Enter your function here"
        helper_text: "use parameters for best results, ex: 5*(x^2)*sin(x)"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:270
        id:  textfieldEcart   
    MDRectangleFlatButton:
        text:'calculate'
        pos_hint:{'center_x': 0.5, 'center_y': 0.3}
        on_release: app.root.get_screen("EGcar").change_variable(textfieldEcart.text)

<EGcyl>:
    name:'EGcyl'
    MDLabel:
        text: 'E = −grad V using cylindrical coordinates'
        halign:'center'
        pos_hint: {"center_y": 0.9}
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 

    MDLabel:
        text: 'for easy input, click on the following to copy the symbol:'
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 1
        halign:'center'
        pos_hint: {'center_y':0.8}
        
        

    MDRoundFlatButton:
        text:'ρ'
        id:  pgp_text 
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        on_release: app.root.get_screen("LapCordCyl").symbols_p(pgp_text.text)


    MDRoundFlatButton:
        text:'φ'
        id:  abaa_text 
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        on_release: app.root.get_screen("LapCordCyl").symbols_phai(abaa_text.text)

    MDRectangleFlatButton:
        text:"Main Menu"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'MainMenu'

    MDTextField:
        hint_text: "Enter your function here"
        helper_text: "use parameters for best results, ex: 5*(ρ^2)*sin(φ)"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:270
        id:  textfieldGrade_cyl  
    MDRectangleFlatButton:
        text:'calculate'
        pos_hint:{'center_x': 0.5, 'center_y': 0.3}
        on_release: app.root.get_screen("EGcyl").change_variable(textfieldGrade_cyl.text)

<EGsph>:
    name:'EGsph'
    MDLabel:
        text: 'Gradient of V in spherical coordinates'
        halign:'center'
        pos_hint: {"center_y": 0.9}
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 

    MDLabel:
        text: 'for easy input, click on the following to copy the symbol:'
        theme_text_color: "Custom"
        text_color: 1, 196/255, 0, 1
        halign:'center'
        pos_hint: {'center_y':0.8}

    

    MDRectangleFlatButton:
        text:"Main Menu"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'MainMenu'
        
    MDRoundFlatButton:
        text:'θ'
        id:  aa_a_text 
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        on_release: app.root.get_screen("LapCordSph").symbols_theta(aa_a_text.text)


    MDRoundFlatButton:
        text:'φ'
        id:  aqaq_text 
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        on_release: app.root.get_screen("LapCordCyl").symbols_phai(aqaq_text.text)    

    MDTextField:
        hint_text: "Enter your function here"
        helper_text: "use parameters for best results, ex: 5*(r^2)*sin(θ)"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:270
        id:  textfieldGradCordSphe_sph   
    MDRectangleFlatButton:
        text:'calculate'
        pos_hint:{'center_x': 0.5, 'center_y': 0.3}
        on_release: app.root.get_screen("EGsph").change_variable(textfieldGradCordSphe_sph.text)         
                                             

"""


class MenuScreen(Screen):
    pass


class LapCordScreen(Screen):
    pass


class LapCordCar(Screen):

    def change_variable(self, obj):
        dxx = diff(obj, x, x)
        dyy = diff(obj, y, y)
        dzz = diff(obj, z, z)
        lap_car_result = dxx + dyy + dzz + 0
        self.dialog = MDDialog(title='result',
                               text=str(lap_car_result),

                               size_hint=(0.8, 1),
                               buttons=[MDFlatButton(text='Close',

                                                     on_release=self.close_dialog)]
                               )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


class LapCordCyl(Screen):
    def change_variable(self, obj):
        dpp_lap = ((1 / ρ) * diff((ρ * diff(obj, ρ)), ρ))
        dqq_lap = ((1 / (p * p)) * diff(obj, φ, φ))
        dzz_lap = diff(obj, z, z)
        Grad_car_result = dpp_lap + dqq_lap + dzz_lap
        self.dialog = MDDialog(
            text=str(Grad_car_result),

            size_hint=(0.8, 1),
            buttons=[MDFlatButton(text='Close',

                                  on_release=self.close_dialog)]
        )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def symbols_p(self, obj):
        p = copy('ρ')
        return p

    def symbols_phai(self, obj):
        phai = copy('φ')
        return phai


class LapCordSph(Screen):
    def change_variable(self, obj):
        drr_lap = ((1 / (r * r)) * diff(((r * r) * diff(obj, r)), r))
        daa_lap = ((1 / (r * r * sin(θ))) * diff(sin(θ) * diff(obj, θ), θ))
        dqqs_lap = ((1 / (r * r * sin(θ) * sin(θ))) * diff(obj, φ, φ))
        lap_car_result = drr_lap + daa_lap + dqqs_lap
        self.dialog = MDDialog(title='result',
                               text=str(lap_car_result),

                               size_hint=(0.8, 1),
                               buttons=[MDFlatButton(text='Close',

                                                     on_release=self.close_dialog)]
                               )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def symbols_theta(self, obj):
        theta = copy('θ')
        return theta


class GradCordScreen(Screen):
    pass


class EGcord(Screen):
    pass


class EGcar(Screen):
    def change_variable(self, obj):
        dx_e = -diff(obj, x)
        dy_e = -diff(obj, y)
        dz_e = -diff(obj, z)
        Grad_car_result = str(
            "(" + str(dx_e) + ")" + "ax + " + "(" + str(dy_e) + ")" + "ay +  " + "(" + str(dz_e) + ")" + "az")
        self.dialog = MDDialog(title='result',
                               text=Grad_car_result,

                               size_hint=(0.8, 1),
                               buttons=[MDFlatButton(text='Close',

                                                     on_release=self.close_dialog)]
                               )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


class EGcyl(Screen):
    def change_variable(self, obj):
        dp_gr = -diff(obj, ρ)
        dq_gr = -((1 / ρ) * diff(obj, φ))
        dz_gr = -diff(obj, z)
        Gradd_car_result = str(
            "(" + str(dp_gr) + ")" + "aρ + " + "(" + str(dq_gr) + ")" + "aφ +  " + "(" + str(dz_gr) + ")" + "az")
        self.dialog = MDDialog(title='result',
                               text=Gradd_car_result,

                               size_hint=(0.8, 1),
                               buttons=[MDFlatButton(text='Close',

                                                     on_release=self.close_dialog)]
                               )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


class EGsph(Screen):
    def change_variable(self, obj):
        dr_gr_s = -diff(obj, r)
        da_gr_ss = -((1 / r) * diff(obj, θ))
        dq_gr_sss = -(1 / (r * sin(θ))) * diff(obj, φ)
        Gradd_car_result = str(
            "(" + str(dr_gr_s) + ")" + "ar + " + "(" + str(da_gr_ss) + ")" + "aθ +  " + "(" + str(
                dq_gr_sss) + ")" + "aφ")
        self.dialog = MDDialog(title='result',
                               text=Gradd_car_result,

                               size_hint=(0.8, 1),
                               buttons=[MDFlatButton(text='Close',

                                                     on_release=self.close_dialog)]
                               )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


class GradCordCar(Screen):
    def change_variable(self, obj):
        dx = diff(obj, x)
        dy = diff(obj, y)
        dz = diff(obj, z)
        Grad_car_result = str(
            "(" + str(dx) + ")" + "ax + " + "(" + str(dy) + ")" + "ay +  " + "(" + str(dz) + ")" + "az")
        self.dialog = MDDialog(title='result',
                               text=Grad_car_result,

                               size_hint=(0.8, 1),
                               buttons=[MDFlatButton(text='Close',

                                                     on_release=self.close_dialog)]
                               )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


class GradCordCyl(Screen):
    def change_variable(self, obj):
        dp_gr = diff(obj, ρ)
        dq_gr = ((1 / ρ) * diff(obj, φ))
        dz_gr = diff(obj, z)
        Gradd_car_result = str(
            "(" + str(dp_gr) + ")" + "aρ + " + "(" + str(dq_gr) + ")" + "aφ +  " + "(" + str(dz_gr) + ")" + "az")
        self.dialog = MDDialog(title='result',
                               text=Gradd_car_result,

                               size_hint=(0.8, 1),
                               buttons=[MDFlatButton(text='Close',

                                                     on_release=self.close_dialog)]
                               )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


class GradCordSph(Screen):
    def change_variable(self, obj):
        dr_gr_s = diff(obj, r)
        da_gr_ss = ((1 / r) * diff(obj, θ))
        dq_gr_sss = (1 / (r * sin(θ))) * diff(obj, φ)
        Gradd_car_result = str(
            "(" + str(dr_gr_s) + ")" + "ar + " + "(" + str(da_gr_ss) + ")" + "aθ +  " + "(" + str(
                dq_gr_sss) + ")" + "aφ")
        self.dialog = MDDialog(title='result',
                               text=Gradd_car_result,

                               size_hint=(0.8, 1),
                               buttons=[MDFlatButton(text='Close',

                                                     on_release=self.close_dialog)]
                               )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


class LapCordFORM(Screen):
    def change_variable(self, obj):
        return


class GradCordFORM(Screen):
    def change_variable(self, obj):
        return


class AboutScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='MainMenu'))
sm.add_widget(AboutScreen(name='About'))
sm.add_widget(LapCordScreen(name='LapCordScreen'))
sm.add_widget(LapCordCar(name='LapCordCar'))
sm.add_widget(LapCordCyl(name='LapCordCyl'))
sm.add_widget(LapCordSph(name='LapCordSph'))
sm.add_widget(GradCordCar(name='LapCordCar'))
sm.add_widget(GradCordCyl(name='LapCordCyl'))
sm.add_widget(GradCordSph(name='LapCordSph'))
sm.add_widget(GradCordScreen(name='GradCordScreen'))


class EEproject(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Yellow'
        self.theme_cls.primary_hue = '800'
        self.theme_cls.theme_style = 'Dark'

        screen = Builder.load_string(screen_helper)
        return screen




EEproject().run()
