package com.example.lookify.repositories;

import java.util.List;

import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.example.lookify.models.Song;

@Repository
public interface SongRepo extends CrudRepository<Song, Long> {
	

	// this method retrieves all the songs from the database
	List<Song> findAll();
	

	// this method Get song from database ordred by rating and limit to 10
	@Query(value = "SELECT * FROM songs ORDER BY rating DESC LIMIT 10", nativeQuery = true) 
	List<Song> getTopTen();

	// this method retrieves all songs from the database where artist contains the search string
	List<Song> findByArtistContaining(String artist);
}
