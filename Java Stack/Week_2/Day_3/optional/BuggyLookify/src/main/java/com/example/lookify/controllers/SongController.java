package com.example.lookify.controllers;

import java.util.List;

import jakarta.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.example.lookify.models.Song;
import com.example.lookify.services.SongService;

@Controller
public class SongController {
	// dependency injection for SongService
	@Autowired
	SongService songService;
	// index route
	@GetMapping("/")
	public String index() {
		return "index.jsp";
	}
	

	// dashboard route
	@GetMapping("/dashboard")
	public String dashboard(String artist, Model model) {
		List<Song> songs = songService.allSongs();
		model.addAttribute("songs", songs);
		return "dashboard.jsp";
	}
	// search route
	@GetMapping("/search")
	public String search(@RequestParam("artist") String artist, Model model) {
		List<Song> songs = songService.searchByArtist(artist);
		model.addAttribute("songs", songs);
		return "search.jsp";
	}
	
	// add song route Get for form
	@GetMapping("/songs/new")
	public String addSong(@ModelAttribute("song") Song song) {
		return "add.jsp";
	}
	
	// add song route Post for form
	@PostMapping("/songs/new")
	public String addSong(@Valid @ModelAttribute("song") Song song, BindingResult result) {
		if(result.hasErrors()) {
			return "add.jsp";
		}else {
			songService.addSong(song);
			return "redirect:/dashboard";
		}
	}
	

	// details route 
	@GetMapping("/songs/{id}")
	public String details(@PathVariable("id") Long id, Model model) {
		Song song = songService.findSong(id);
		model.addAttribute("song", song);
		return "details.jsp";
	}
	
	// top ten route
	@GetMapping("/top-ten")
	public String details(Model model) {
		List<Song> songs = songService.topTen();
		model.addAttribute("songs", songs);
		return "top.jsp";
	}
	
	// delete route
	@RequestMapping("/songs/{id}/delete")
	public String deleteSong(@PathVariable("id") Long id) {
		songService.deleteSong(songService.findSong(id));
		return "redirect:/dashboard";
	}
	
}
