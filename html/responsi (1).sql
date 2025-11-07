-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 07 Nov 2025 pada 09.10
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `responsi`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `projects`
--

CREATE TABLE `projects` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `projects`
--

INSERT INTO `projects` (`id`, `title`, `description`) VALUES
(1, 'Proyek Game 2D', 'Waktu SMA, saya mengikuti proyek pelajar Pancasila dengan membuat game 2D sederhana menggunakan Visual Basic Studio. Dalam proyek ini, saya membuat game bertema lingkungan, di mana pemain mengarahkan karakter untuk memungut sampah yang berserakan ke kanan, kiri, atau posisi tertentu. Proyek ini memberikan pengalaman langsung dalam pemrograman dasar, logika permainan, serta desain antarmuka interaktif yang sederhana, sekaligus menanamkan nilai kepedulian terhadap lingkungan dan kerja sama sebagai pelajar Pancasila.');

-- --------------------------------------------------------

--
-- Struktur dari tabel `skills`
--

CREATE TABLE `skills` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `level` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `skills`
--

INSERT INTO `skills` (`id`, `name`, `level`) VALUES
(1, 'Python', 'Menengah'),
(2, 'HTML & CSS', 'Pemula'),
(3, 'Flask', 'Pemula'),
(4, 'Canva', 'Mahir'),
(13, 'Capcut', 'Mahir');

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(100) NOT NULL,
  `bio` text NOT NULL,
  `photo` varchar(255) DEFAULT '''https://drive.google.com/uc?export=view&id=18RgfYVlV3DS3mm4XiFwRLdj6-o9QF3rg'''
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `name`, `bio`, `photo`) VALUES
(1, 'joseph123', 'josephgian', 'Joseph Gian Maresyembun', 'Saya adalah Joseph Gian, seorang mahasiswa Informatika di Universitas Teknologi Yogyakarta. Saya berasal dari Ambon dan merupakan pribadi yang memiliki semangat tinggi dalam menimba ilmu. Saya dikenal sebagai individu yang disiplin, bertanggung jawab, serta berkomitmen untuk selalu memberikan hasil terbaik dalam setiap kegiatan yang saya jalani. Selain itu, saya memiliki minat dalam bidang desain dan multimedia. Saya senang mengedit berbagai jenis konten menggunakan aplikasi seperti Canva, CapCut, dan media kreatif lainnya.\r\n', 'foto2.jpg');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `projects`
--
ALTER TABLE `projects`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `skills`
--
ALTER TABLE `skills`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `projects`
--
ALTER TABLE `projects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `skills`
--
ALTER TABLE `skills`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
