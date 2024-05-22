package com.example.demo.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;


@Controller
public class HopperReceipt {
	
    @RequestMapping("/")
    public String index(Model model) {
        
        // Create attributes
        String name = "Grace Hopper";
        String itemName = "Copper wire";
        double price = 5.25;
        String description = "Metal strips, also an illustration of nanoseconds.";
        String vendor = "Little Things Corner Store";

        // Add attributes to the model
        model.addAttribute("name", name);
        model.addAttribute("itemName", itemName);
        model.addAttribute("price", price);
        model.addAttribute("description", description);
        model.addAttribute("vendor", vendor);

        //second test attributes
        String name2 = "Dark Vador";
        String itemName2 = "Light Saber";
        double price2 = 1000.00;
        String description2 = "The weapon of a Jedi Knight. Not as clumsy or random as a blaster. An elegant weapon for a more civilized age.";
        String vendor2 = "Galactic Empire";

        // Add attributes second test to the model
        model.addAttribute("name2", name2);
        model.addAttribute("itemName2", itemName2);
        model.addAttribute("price2", price2);
        model.addAttribute("description2", description2);
        model.addAttribute("vendor2", vendor2);
    
        return "index.jsp";
    }
    //...
    


}
