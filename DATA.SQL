INSERT INTO mc_users (name, lastname) VALUES
('Steve', 'Blockhead'),
('Alex', 'Pickaxe'),
('Herobrine', 'Spooky'),
('Creeper', 'Boom'),
('Notch', 'Legend'),
('Ender', 'Maniac'),
('Villager', 'Hmmm'),
('Bob', 'Builder'),
('Dirt', 'Master'),
('Diamond', 'Hunter');

INSERT INTO mc_logins (username, password, user_id) VALUES
('SteveTheNoob', 'password123', 1),
('AlexTheGreat', 'diamonds4ever', 2),
('xXHerobrineXx', 'spookyGhosts', 3),
('CreeperKiller99', 'sssssBOOM', 4),
('KingNotch', 'mojangRocks', 5),
('EndermanIsHere', 'dontLookAtMe', 6),
('Villager123', 'hmmmmmm', 7),
('BobDaBuilder', 'yesWeCan', 8),
('DirtLover420', 'mudLife', 9),
('DiamondGod', 'shineBright', 10);

INSERT INTO mc_srv_types (name) VALUES
('Survival'),
('Creative'),
('Hardcore'),
('MiniGames'),
('RPG'),
('PvP'),
('Skyblock');

INSERT INTO mc_srv_versions (version) VALUES
('1.20.4'),
('1.19.2'),
('1.18.1'),
('1.16.5'),
('1.12.2'),
('1.8.9');

INSERT INTO mc_servers_list (
    login_id, ip, port, description, publication_date, update_date, version,
    players_online, players_max, favicon, server_views
) VALUES
(1, 'mc.hypixel.net', 25565, 'Hypixel megaspace', '2025-04-08', '2025-04-08', '1.20.4', 50000, 100000, '', 10234),
(2, 'play.cubecraft.net', 25565, 'CubeCraft LOLs', '2025-04-08', '2025-04-08', '1.19.2', 15000, 50000, '', 5230),
(3, 'mc.funville.net', 25565, 'Funville Adventures', '2025-04-08', '2025-04-08', '1.18.1', 1200, 3000, '', 894),
(4, '192.168.0.4', 25565, 'Adventure quest', '2025-04-08', '2025-04-08', '1.21', 10, 30, '', 12),
(5, 'mc.blockparty.net', 25565, 'Dancing with Creepers', '2025-04-08', '2025-04-08', '1.16.5', 500, 1000, '', 666),
(6, 'mc.epicstuff.net', 25565, 'Totally not sus', '2025-04-08', '2025-04-08', '1.8.9', 200, 400, '', 987),
(7, 'play.cakewars.net', 25565, 'Free cake for all!', '2025-04-08', '2025-04-08', '1.12.2', 50, 100, '', 33),
(8, '192.168.0.8', 25565, 'Bedwars but chaotic', '2025-04-08', '2025-04-08', '1.20', 15, 40, '', 24),
(9, 'mc.memecraft.gg', 25565, 'Shrek is love, Shrek is server', '2025-04-08', '2025-04-08', '1.19.4', 4, 20, '', 69),
(10, '192.168.0.10', 25565, 'LagZone Extreme', '2025-04-08', '2025-04-08', '1.17', 2, 10, '', 7);

INSERT INTO mc_liked_servers (login_id, server_id, vote) VALUES
(1, 1, 1),
(2, 1, -1),
(3, 2, 1),
(4, 3, 1),
(5, 3, -1),
(6, 4, 1),
(7, 5, 0),
(8, 2, 1),
(9, 5, -1),
(10, 1, 1);

INSERT INTO mc_server_reviews (review, server_id, login_id, created_at_date, created_at_time) VALUES
('10/10 would explode again!', 1, 4, '2025-04-09', '12:00:00'),
('This server gave me diamonds. I’m in love.', 1, 10, '2025-04-08', '10:30:00'),
('Pixelmon is life!', 4, 3, '2025-04-07', '14:15:00'),
('Too many cubes. Got lost.', 2, 7, '2025-04-06', '16:45:00'),
('I sneezed and got banned.', 3, 2, '2025-04-05', '18:20:00'),
('Server’s fine, my skills aren’t.', 5, 6, '2025-04-04', '19:00:00'),
('I built a dirt mansion. Flex.', 5, 9, '2025-04-03', '11:11:00'),
('Cool PvP, but lag made me cry.', 2, 8, '2025-04-02', '09:00:00'),
('Accidentally punched a villager. Whole town attacked me.', 1, 6, '2025-04-01', '13:37:00'),
('I tamed a wolf and named it Jeff. 10/10.', 2, 5, '2025-04-01', '14:05:00'),
('This place smells like redstone.', 3, 1, '2025-03-31', '12:00:00'),
('I tried to swim in lava. Did not work.', 4, 8, '2025-03-30', '17:25:00'),
('Cake is a lie. There was no cake.', 7, 7, '2025-03-29', '20:15:00'),
('Built a skybase, immediately fell. Gravity is OP.', 2, 4, '2025-03-28', '09:45:00'),
('Everyone here is nice, except for Jerry. Jerry griefed me.', 5, 2, '2025-03-27', '16:30:00'),
('Great place to chill. I AFK’d for 3 hours.', 6, 10, '2025-03-26', '15:00:00'),
('This server runs smoother than my fridge.', 8, 9, '2025-03-25', '11:42:00'),
('I saw Herobrine. Or maybe just Steve with a bug.', 1, 3, '2025-03-24', '21:20:00'),
('Server gave me a diamond. I cried.', 3, 5, '2025-03-23', '08:08:00'),
('I ate 6 golden apples and still lost. Hacker?', 6, 1, '2025-03-22', '10:10:10'),
('This place feels like home. If home was full of creepers.', 9, 6, '2025-03-21', '22:22:22'),
('Too many chickens. It’s terrifying.', 10, 8, '2025-03-20', '12:12:12'),
('Server crashed. I blame Bob.', 4, 7, '2025-03-19', '07:07:07');

INSERT INTO mc_servers_list_server_type (minecraftserver_id, servertype_id) VALUES
(1, 4),
(1, 6),
(2, 4),
(2, 1),
(3, 1),
(3, 6),
(4, 5),
(5, 1);

INSERT INTO mc_servers_list_server_version (minecraftserver_id, serverversion_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 6);
