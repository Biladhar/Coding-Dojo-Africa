package com.caresoft.clinicapp;

import java.util.ArrayList;
import java.util.Date;

public class AdminUser extends User implements HIPAACompliantUser, HIPAACompliantAdmin {
	private Integer employeeID;
    private String role;
    private ArrayList<String> securityIncidents;
    
    // TO DO: Implement a constructor that takes an ID and a role
    public AdminUser(Integer employeeID, String role) {
        this.employeeID = employeeID;
        this.role = role;
    }
    

    // TO DO: Implement HIPAACompliantUser!
    public boolean assignPin(int pin) {
        if (pin >= 1000 && pin <= 9999) {
            return true;
        }
        return false;
    }
    // TO DO: Implement HIPAACompliantAdmin!
    public boolean isAuthorized(Integer confirmedAuthID) {
        if (confirmedAuthID == this.employeeID) {
            return true;
        }
        return false;
    }
    
    public void newIncident(String notes) {
        String report = String.format(
            "Datetime Submitted: %s \n,  Reported By ID: %s\n Notes: %s \n", 
            new Date(), this.id, notes
        );
        securityIncidents.add(report);
    }
    public void authIncident() {
        String report = String.format(
            "Datetime Submitted: %s \n,  ID: %s\n Notes: %s \n", 
            new Date(), this.id, "AUTHORIZATION ATTEMPT FAILED FOR THIS USER"
        );
        securityIncidents.add(report);
    }
    
    // TO DO: Setters & Getters
}
