package com.example.lookify.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.example.lookify.models.Song;
import com.example.lookify.repositories.SongRepo;

@Service
public class SongService {
	// dependency injection for SongRepo
	private final SongRepo songRepo;
	public SongService(SongRepo songRepo) {
		this.songRepo = songRepo;
	}
	
	//! methods

	// this method retrieves all the songs from the database
	public List<Song> allSongs(){
		return songRepo.findAll();
	}
	
	// this method adds a song to the database
	public Song addSong(Song song) {
		return songRepo.save(song);
	}
	

	// this method retrieves a song by id
	public Song findSong(Long id) {
		Optional<Song> optionalSong = songRepo.findById(id);
		if(optionalSong.isPresent()) {
			return optionalSong.get();
		}else {
			return null;
		}
	}
	

	// this method retrieves the top ten songs from the database
	public List<Song> topTen() {
		return songRepo.getTopTen();
	}
	

	// this method updates a song
	public Song updateSong(Song song) {
		return songRepo.save(song);
	}
	

	// this method deletes a song
	public void deleteSong(Song song) {
		songRepo.delete(song);
	}


	// this method retrieves all songs from the database where artist contains the search string
	public List<Song> searchByArtist(String artist) {
		return songRepo.findByArtistContaining(artist);
	}
}
