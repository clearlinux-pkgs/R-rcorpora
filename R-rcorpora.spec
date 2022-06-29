#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rcorpora
Version  : 2.0.0
Release  : 4
URL      : https://cran.r-project.org/src/contrib/rcorpora_2.0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rcorpora_2.0.0.tar.gz
Summary  : A Collection of Small Text Corpora of Interesting Data
Group    : Development/Tools
License  : CC0-1.0
Requires: R-jsonlite
BuildRequires : R-jsonlite
BuildRequires : buildreq-R

%description
# rcorpora
[![Linux Build Status](https://travis-ci.org/gaborcsardi/rcorpora.svg?branch=master)](https://travis-ci.org/gaborcsardi/rcorpora)
[![Windows Build status](https://ci.appveyor.com/api/projects/status/github/gaborcsardi/rcorpora?svg=true)](https://ci.appveyor.com/project/gaborcsardi/rcorpora)
[![CRAN version](http://www.r-pkg.org/badges/version/rcorpora)](http://www.r-pkg.org/pkg/rcorpora)
[![CRAN RStudio mirror downloads](http://cranlogs.r-pkg.org/badges/rcorpora)](http://cran.r-project.org/web/packages/rcorpora/index.html)

%prep
%setup -q -c -n rcorpora
cd %{_builddir}/rcorpora

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641089282

%install
export SOURCE_DATE_EPOCH=1641089282
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rcorpora
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rcorpora
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rcorpora
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rcorpora || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rcorpora/DESCRIPTION
/usr/lib64/R/library/rcorpora/INDEX
/usr/lib64/R/library/rcorpora/Meta/Rd.rds
/usr/lib64/R/library/rcorpora/Meta/features.rds
/usr/lib64/R/library/rcorpora/Meta/hsearch.rds
/usr/lib64/R/library/rcorpora/Meta/links.rds
/usr/lib64/R/library/rcorpora/Meta/nsInfo.rds
/usr/lib64/R/library/rcorpora/Meta/package.rds
/usr/lib64/R/library/rcorpora/NAMESPACE
/usr/lib64/R/library/rcorpora/NEWS.md
/usr/lib64/R/library/rcorpora/R/rcorpora
/usr/lib64/R/library/rcorpora/R/rcorpora.rdb
/usr/lib64/R/library/rcorpora/R/rcorpora.rdx
/usr/lib64/R/library/rcorpora/README.markdown
/usr/lib64/R/library/rcorpora/corpora/Gruntfile.js
/usr/lib64/R/library/rcorpora/corpora/README.md
/usr/lib64/R/library/rcorpora/corpora/data/animals/birds_antarctica.json
/usr/lib64/R/library/rcorpora/corpora/data/animals/birds_north_america.json
/usr/lib64/R/library/rcorpora/corpora/data/animals/cats.json
/usr/lib64/R/library/rcorpora/corpora/data/animals/collateral_adjectives.json
/usr/lib64/R/library/rcorpora/corpora/data/animals/common.json
/usr/lib64/R/library/rcorpora/corpora/data/animals/dinosaurs.json
/usr/lib64/R/library/rcorpora/corpora/data/animals/dog_names.json
/usr/lib64/R/library/rcorpora/corpora/data/animals/dogs.json
/usr/lib64/R/library/rcorpora/corpora/data/animals/donkeys.json
/usr/lib64/R/library/rcorpora/corpora/data/animals/horses.json
/usr/lib64/R/library/rcorpora/corpora/data/animals/ponies.json
/usr/lib64/R/library/rcorpora/corpora/data/archetypes/artifact.json
/usr/lib64/R/library/rcorpora/corpora/data/archetypes/character.json
/usr/lib64/R/library/rcorpora/corpora/data/archetypes/event.json
/usr/lib64/R/library/rcorpora/corpora/data/archetypes/setting.json
/usr/lib64/R/library/rcorpora/corpora/data/architecture/passages.json
/usr/lib64/R/library/rcorpora/corpora/data/architecture/rooms.json
/usr/lib64/R/library/rcorpora/corpora/data/art/isms.json
/usr/lib64/R/library/rcorpora/corpora/data/colors/crayola.json
/usr/lib64/R/library/rcorpora/corpora/data/colors/dulux.json
/usr/lib64/R/library/rcorpora/corpora/data/colors/google_material_colors.json
/usr/lib64/R/library/rcorpora/corpora/data/colors/paints.json
/usr/lib64/R/library/rcorpora/corpora/data/colors/palettes.json
/usr/lib64/R/library/rcorpora/corpora/data/colors/web_colors.json
/usr/lib64/R/library/rcorpora/corpora/data/colors/xkcd.json
/usr/lib64/R/library/rcorpora/corpora/data/corporations/cars.json
/usr/lib64/R/library/rcorpora/corpora/data/corporations/djia.json
/usr/lib64/R/library/rcorpora/corpora/data/corporations/fortune500.json
/usr/lib64/R/library/rcorpora/corpora/data/corporations/industries.json
/usr/lib64/R/library/rcorpora/corpora/data/corporations/nasdaq.json
/usr/lib64/R/library/rcorpora/corpora/data/corporations/newspapers.json
/usr/lib64/R/library/rcorpora/corpora/data/divination/tarot_interpretations.json
/usr/lib64/R/library/rcorpora/corpora/data/divination/zodiac.json
/usr/lib64/R/library/rcorpora/corpora/data/film-tv/game-of-thrones-houses.json
/usr/lib64/R/library/rcorpora/corpora/data/film-tv/iab_categories.json
/usr/lib64/R/library/rcorpora/corpora/data/film-tv/netflix-categories.json
/usr/lib64/R/library/rcorpora/corpora/data/film-tv/popular-movies.json
/usr/lib64/R/library/rcorpora/corpora/data/film-tv/tv_shows.json
/usr/lib64/R/library/rcorpora/corpora/data/foods/apple_cultivars.json
/usr/lib64/R/library/rcorpora/corpora/data/foods/bad_beers.json
/usr/lib64/R/library/rcorpora/corpora/data/foods/beer_categories.json
/usr/lib64/R/library/rcorpora/corpora/data/foods/beer_styles.json
/usr/lib64/R/library/rcorpora/corpora/data/foods/breads_and_pastries.json
/usr/lib64/R/library/rcorpora/corpora/data/foods/combine.json
/usr/lib64/R/library/rcorpora/corpora/data/foods/condiments.json
/usr/lib64/R/library/rcorpora/corpora/data/foods/curds.json
/usr/lib64/R/library/rcorpora/corpora/data/foods/fruits.json
/usr/lib64/R/library/rcorpora/corpora/data/foods/herbs_n_spices.json
/usr/lib64/R/library/rcorpora/corpora/data/foods/hot_peppers.json
/usr/lib64/R/library/rcorpora/corpora/data/foods/iba_cocktails.json
/usr/lib64/R/library/rcorpora/corpora/data/foods/menuItems.json
/usr/lib64/R/library/rcorpora/corpora/data/foods/pizzaToppings.json
/usr/lib64/R/library/rcorpora/corpora/data/foods/sandwiches.json
/usr/lib64/R/library/rcorpora/corpora/data/foods/sausages.json
/usr/lib64/R/library/rcorpora/corpora/data/foods/scotch_whiskey.json
/usr/lib64/R/library/rcorpora/corpora/data/foods/tea.json
/usr/lib64/R/library/rcorpora/corpora/data/foods/vegetable_cooking_times.json
/usr/lib64/R/library/rcorpora/corpora/data/foods/vegetables.json
/usr/lib64/R/library/rcorpora/corpora/data/foods/wine_descriptions.json
/usr/lib64/R/library/rcorpora/corpora/data/games/bannedGames/argentina/bannedList.json
/usr/lib64/R/library/rcorpora/corpora/data/games/bannedGames/brazil/bannedList.json
/usr/lib64/R/library/rcorpora/corpora/data/games/bannedGames/china/bannedList.json
/usr/lib64/R/library/rcorpora/corpora/data/games/bannedGames/denmark/bannedList.json
/usr/lib64/R/library/rcorpora/corpora/data/games/cluedo.json
/usr/lib64/R/library/rcorpora/corpora/data/games/dark_souls_iii_messages.json
/usr/lib64/R/library/rcorpora/corpora/data/games/jeopardy_questions.json
/usr/lib64/R/library/rcorpora/corpora/data/games/pokemon.json
/usr/lib64/R/library/rcorpora/corpora/data/games/scrabble.json
/usr/lib64/R/library/rcorpora/corpora/data/games/street_fighter_ii.json
/usr/lib64/R/library/rcorpora/corpora/data/games/trivial_pursuit.json
/usr/lib64/R/library/rcorpora/corpora/data/games/wrestling_moves.json
/usr/lib64/R/library/rcorpora/corpora/data/games/zelda.json
/usr/lib64/R/library/rcorpora/corpora/data/geography/canada_provinces_and_territories.json
/usr/lib64/R/library/rcorpora/corpora/data/geography/canadian_municipalities.json
/usr/lib64/R/library/rcorpora/corpora/data/geography/countries.json
/usr/lib64/R/library/rcorpora/corpora/data/geography/countries_with_capitals.json
/usr/lib64/R/library/rcorpora/corpora/data/geography/english_towns_cities.json
/usr/lib64/R/library/rcorpora/corpora/data/geography/japanese_prefectures.json
/usr/lib64/R/library/rcorpora/corpora/data/geography/london_underground_stations.json
/usr/lib64/R/library/rcorpora/corpora/data/geography/nationalities.json
/usr/lib64/R/library/rcorpora/corpora/data/geography/norwegian_cities.json
/usr/lib64/R/library/rcorpora/corpora/data/geography/nyc_neighborhood_zips.json
/usr/lib64/R/library/rcorpora/corpora/data/geography/oceans.json
/usr/lib64/R/library/rcorpora/corpora/data/geography/rivers.json
/usr/lib64/R/library/rcorpora/corpora/data/geography/sf_neighborhoods.json
/usr/lib64/R/library/rcorpora/corpora/data/geography/us_airport_codes.json
/usr/lib64/R/library/rcorpora/corpora/data/geography/us_cities.json
/usr/lib64/R/library/rcorpora/corpora/data/geography/us_counties.json
/usr/lib64/R/library/rcorpora/corpora/data/geography/us_metropolitan_areas.json
/usr/lib64/R/library/rcorpora/corpora/data/geography/us_state_capitals.json
/usr/lib64/R/library/rcorpora/corpora/data/geography/venues.json
/usr/lib64/R/library/rcorpora/corpora/data/geography/winds.json
/usr/lib64/R/library/rcorpora/corpora/data/governments/mass-surveillance-project-names.json
/usr/lib64/R/library/rcorpora/corpora/data/governments/nsa_projects.json
/usr/lib64/R/library/rcorpora/corpora/data/governments/uk_political_parties.json
/usr/lib64/R/library/rcorpora/corpora/data/governments/us_federal_agencies.json
/usr/lib64/R/library/rcorpora/corpora/data/governments/us_mil_operations.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/2016_us_presidential_candidates.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/atus_activities.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/authors.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/bodyParts.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/britishActors.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/celebrities.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/descriptions.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/englishHonorifics.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/famousDuos.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/firstNames.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/lastNames.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/moods.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/norwayFirstNamesBoys.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/norwayFirstNamesGirls.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/norwayLastNames.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/occupations.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/prefixes.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/richpeople.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/scientists.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/spanishFirstNames.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/spanishLastNames.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/spinalTapDrummers.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/suffixes.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/thirdPersonPronouns.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/tolkienCharacterNames.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/us_presidents.json
/usr/lib64/R/library/rcorpora/corpora/data/humans/wrestlers.json
/usr/lib64/R/library/rcorpora/corpora/data/instructions/laundry_care.json
/usr/lib64/R/library/rcorpora/corpora/data/materials/abridged-body-fluids.json
/usr/lib64/R/library/rcorpora/corpora/data/materials/building-materials.json
/usr/lib64/R/library/rcorpora/corpora/data/materials/carbon-allotropes.json
/usr/lib64/R/library/rcorpora/corpora/data/materials/decorative-stones.json
/usr/lib64/R/library/rcorpora/corpora/data/materials/fabrics.json
/usr/lib64/R/library/rcorpora/corpora/data/materials/fibers.json
/usr/lib64/R/library/rcorpora/corpora/data/materials/gemstones.json
/usr/lib64/R/library/rcorpora/corpora/data/materials/layperson-metals.json
/usr/lib64/R/library/rcorpora/corpora/data/materials/metals.json
/usr/lib64/R/library/rcorpora/corpora/data/materials/natural-materials.json
/usr/lib64/R/library/rcorpora/corpora/data/materials/packaging.json
/usr/lib64/R/library/rcorpora/corpora/data/materials/plastic-brands.json
/usr/lib64/R/library/rcorpora/corpora/data/materials/sculpture-materials.json
/usr/lib64/R/library/rcorpora/corpora/data/materials/technical-fabrics.json
/usr/lib64/R/library/rcorpora/corpora/data/mathematics/fibonnaciSequence.json
/usr/lib64/R/library/rcorpora/corpora/data/mathematics/primes.json
/usr/lib64/R/library/rcorpora/corpora/data/mathematics/primes_binary.json
/usr/lib64/R/library/rcorpora/corpora/data/mathematics/trigonometry.json
/usr/lib64/R/library/rcorpora/corpora/data/medicine/diagnoses.json
/usr/lib64/R/library/rcorpora/corpora/data/medicine/drugNameStems.json
/usr/lib64/R/library/rcorpora/corpora/data/medicine/drugs.json
/usr/lib64/R/library/rcorpora/corpora/data/medicine/hospitals.json
/usr/lib64/R/library/rcorpora/corpora/data/music/a_list_of_guitar_manufacturers.json
/usr/lib64/R/library/rcorpora/corpora/data/music/bands_that_have_opened_for_tool.json
/usr/lib64/R/library/rcorpora/corpora/data/music/female_classical_guitarists.json
/usr/lib64/R/library/rcorpora/corpora/data/music/genres.json
/usr/lib64/R/library/rcorpora/corpora/data/music/hamilton_musical_obcrecording_actors_characters.json
/usr/lib64/R/library/rcorpora/corpora/data/music/instruments.json
/usr/lib64/R/library/rcorpora/corpora/data/music/mtv_day_one.json
/usr/lib64/R/library/rcorpora/corpora/data/music/rock_hall_of_fame.json
/usr/lib64/R/library/rcorpora/corpora/data/music/xxl_freshman.json
/usr/lib64/R/library/rcorpora/corpora/data/mythology/greek_gods.json
/usr/lib64/R/library/rcorpora/corpora/data/mythology/greek_monsters.json
/usr/lib64/R/library/rcorpora/corpora/data/mythology/greek_myths_master.json
/usr/lib64/R/library/rcorpora/corpora/data/mythology/greek_titans.json
/usr/lib64/R/library/rcorpora/corpora/data/mythology/hebrew_god.json
/usr/lib64/R/library/rcorpora/corpora/data/mythology/lovecraft.json
/usr/lib64/R/library/rcorpora/corpora/data/mythology/monsters.json
/usr/lib64/R/library/rcorpora/corpora/data/mythology/norse_gods.json
/usr/lib64/R/library/rcorpora/corpora/data/objects/clothing.json
/usr/lib64/R/library/rcorpora/corpora/data/objects/corpora_winners.json
/usr/lib64/R/library/rcorpora/corpora/data/objects/objects.json
/usr/lib64/R/library/rcorpora/corpora/data/plants/cannabis.json
/usr/lib64/R/library/rcorpora/corpora/data/plants/flowers.json
/usr/lib64/R/library/rcorpora/corpora/data/plants/plants.json
/usr/lib64/R/library/rcorpora/corpora/data/religion/christian_saints.json
/usr/lib64/R/library/rcorpora/corpora/data/religion/fictional_religions.json
/usr/lib64/R/library/rcorpora/corpora/data/religion/parody_religions.json
/usr/lib64/R/library/rcorpora/corpora/data/religion/religions.json
/usr/lib64/R/library/rcorpora/corpora/data/science/elements.json
/usr/lib64/R/library/rcorpora/corpora/data/science/hail_size.json
/usr/lib64/R/library/rcorpora/corpora/data/science/minor_planets.json
/usr/lib64/R/library/rcorpora/corpora/data/science/planets.json
/usr/lib64/R/library/rcorpora/corpora/data/science/pregnancy.json
/usr/lib64/R/library/rcorpora/corpora/data/science/toxic_chemicals.json
/usr/lib64/R/library/rcorpora/corpora/data/science/weather_conditions.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/animal_welfare.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/designated_terrorist_groups/australia.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/designated_terrorist_groups/canada.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/designated_terrorist_groups/china.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/designated_terrorist_groups/egypt.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/designated_terrorist_groups/european_union.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/designated_terrorist_groups/india.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/designated_terrorist_groups/iran.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/designated_terrorist_groups/israel.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/designated_terrorist_groups/kazakhstan.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/designated_terrorist_groups/russia.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/designated_terrorist_groups/saudi_arabia.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/designated_terrorist_groups/tunisia.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/designated_terrorist_groups/turkey.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/designated_terrorist_groups/uae.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/designated_terrorist_groups/ukraine.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/designated_terrorist_groups/united_kingdom.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/designated_terrorist_groups/united_nations.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/designated_terrorist_groups/united_states.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/fraternities/coeducational_fraternities.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/fraternities/defunct.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/fraternities/fraternities.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/fraternities/professional.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/fraternities/service.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/fraternities/sororities.json
/usr/lib64/R/library/rcorpora/corpora/data/societies_and_groups/semi_secret.json
/usr/lib64/R/library/rcorpora/corpora/data/sports/football/epl_teams.json
/usr/lib64/R/library/rcorpora/corpora/data/sports/football/laliga_teams.json
/usr/lib64/R/library/rcorpora/corpora/data/sports/football/serieA.json
/usr/lib64/R/library/rcorpora/corpora/data/sports/mlb_teams.json
/usr/lib64/R/library/rcorpora/corpora/data/sports/nba_mvps.json
/usr/lib64/R/library/rcorpora/corpora/data/sports/nba_teams.json
/usr/lib64/R/library/rcorpora/corpora/data/sports/nfl_teams.json
/usr/lib64/R/library/rcorpora/corpora/data/sports/nhl_teams.json
/usr/lib64/R/library/rcorpora/corpora/data/sports/olympics.json
/usr/lib64/R/library/rcorpora/corpora/data/technology/appliances.json
/usr/lib64/R/library/rcorpora/corpora/data/technology/computer_sciences.json
/usr/lib64/R/library/rcorpora/corpora/data/technology/fireworks.json
/usr/lib64/R/library/rcorpora/corpora/data/technology/guns_n_rifles.json
/usr/lib64/R/library/rcorpora/corpora/data/technology/knots.json
/usr/lib64/R/library/rcorpora/corpora/data/technology/lisp.json
/usr/lib64/R/library/rcorpora/corpora/data/technology/new_technologies.json
/usr/lib64/R/library/rcorpora/corpora/data/technology/photo_sharing_websites.json
/usr/lib64/R/library/rcorpora/corpora/data/technology/programming_languages.json
/usr/lib64/R/library/rcorpora/corpora/data/technology/social_networking_websites.json
/usr/lib64/R/library/rcorpora/corpora/data/technology/video_hosting_websites.json
/usr/lib64/R/library/rcorpora/corpora/data/transportation/commercial-aircraft.json
/usr/lib64/R/library/rcorpora/corpora/data/travel/lcc.json
/usr/lib64/R/library/rcorpora/corpora/data/words/adjs.json
/usr/lib64/R/library/rcorpora/corpora/data/words/adverbs.json
/usr/lib64/R/library/rcorpora/corpora/data/words/closed_pairs.json
/usr/lib64/R/library/rcorpora/corpora/data/words/common.json
/usr/lib64/R/library/rcorpora/corpora/data/words/compounds.json
/usr/lib64/R/library/rcorpora/corpora/data/words/crash_blossoms.json
/usr/lib64/R/library/rcorpora/corpora/data/words/eggcorns.json
/usr/lib64/R/library/rcorpora/corpora/data/words/emoji/cute_kaomoji.json
/usr/lib64/R/library/rcorpora/corpora/data/words/emoji/emoji.json
/usr/lib64/R/library/rcorpora/corpora/data/words/encouraging_words.json
/usr/lib64/R/library/rcorpora/corpora/data/words/ergative_verbs.json
/usr/lib64/R/library/rcorpora/corpora/data/words/expletives.json
/usr/lib64/R/library/rcorpora/corpora/data/words/harvard_sentences.json
/usr/lib64/R/library/rcorpora/corpora/data/words/infinitive_verbs.json
/usr/lib64/R/library/rcorpora/corpora/data/words/interjections.json
/usr/lib64/R/library/rcorpora/corpora/data/words/literature/infinitejest.json
/usr/lib64/R/library/rcorpora/corpora/data/words/literature/lovecraft_words.json
/usr/lib64/R/library/rcorpora/corpora/data/words/literature/mr_men_little_miss.json
/usr/lib64/R/library/rcorpora/corpora/data/words/literature/shakespeare_phrases.json
/usr/lib64/R/library/rcorpora/corpora/data/words/literature/shakespeare_sonnets.json
/usr/lib64/R/library/rcorpora/corpora/data/words/literature/shakespeare_words.json
/usr/lib64/R/library/rcorpora/corpora/data/words/literature/technology_quotes.json
/usr/lib64/R/library/rcorpora/corpora/data/words/nouns.json
/usr/lib64/R/library/rcorpora/corpora/data/words/oprah_quotes.json
/usr/lib64/R/library/rcorpora/corpora/data/words/personal_nouns.json
/usr/lib64/R/library/rcorpora/corpora/data/words/personal_pronouns.json
/usr/lib64/R/library/rcorpora/corpora/data/words/possessive_pronouns.json
/usr/lib64/R/library/rcorpora/corpora/data/words/prefix_root_suffix.json
/usr/lib64/R/library/rcorpora/corpora/data/words/prepositions.json
/usr/lib64/R/library/rcorpora/corpora/data/words/proverbs.json
/usr/lib64/R/library/rcorpora/corpora/data/words/resume_action_words.json
/usr/lib64/R/library/rcorpora/corpora/data/words/rhymeless_words.json
/usr/lib64/R/library/rcorpora/corpora/data/words/spells.json
/usr/lib64/R/library/rcorpora/corpora/data/words/state_verbs.json
/usr/lib64/R/library/rcorpora/corpora/data/words/states_of_drunkenness.json
/usr/lib64/R/library/rcorpora/corpora/data/words/stopwords/ar.json
/usr/lib64/R/library/rcorpora/corpora/data/words/stopwords/bg.json
/usr/lib64/R/library/rcorpora/corpora/data/words/stopwords/cs.json
/usr/lib64/R/library/rcorpora/corpora/data/words/stopwords/da.json
/usr/lib64/R/library/rcorpora/corpora/data/words/stopwords/de.json
/usr/lib64/R/library/rcorpora/corpora/data/words/stopwords/en.json
/usr/lib64/R/library/rcorpora/corpora/data/words/stopwords/es.json
/usr/lib64/R/library/rcorpora/corpora/data/words/stopwords/fi.json
/usr/lib64/R/library/rcorpora/corpora/data/words/stopwords/fr.json
/usr/lib64/R/library/rcorpora/corpora/data/words/stopwords/gr.json
/usr/lib64/R/library/rcorpora/corpora/data/words/stopwords/it.json
/usr/lib64/R/library/rcorpora/corpora/data/words/stopwords/jp.json
/usr/lib64/R/library/rcorpora/corpora/data/words/stopwords/lv.json
/usr/lib64/R/library/rcorpora/corpora/data/words/stopwords/nl.json
/usr/lib64/R/library/rcorpora/corpora/data/words/stopwords/no.json
/usr/lib64/R/library/rcorpora/corpora/data/words/stopwords/pl.json
/usr/lib64/R/library/rcorpora/corpora/data/words/stopwords/pt.json
/usr/lib64/R/library/rcorpora/corpora/data/words/stopwords/ru.json
/usr/lib64/R/library/rcorpora/corpora/data/words/stopwords/sk.json
/usr/lib64/R/library/rcorpora/corpora/data/words/stopwords/sv.json
/usr/lib64/R/library/rcorpora/corpora/data/words/stopwords/tr.json
/usr/lib64/R/library/rcorpora/corpora/data/words/strange_words.json
/usr/lib64/R/library/rcorpora/corpora/data/words/units_of_time.json
/usr/lib64/R/library/rcorpora/corpora/data/words/us_president_quotes.json
/usr/lib64/R/library/rcorpora/corpora/data/words/verbs.json
/usr/lib64/R/library/rcorpora/corpora/data/words/verbs_with_conjugations.json
/usr/lib64/R/library/rcorpora/corpora/data/words/word_clues/clues_five.json
/usr/lib64/R/library/rcorpora/corpora/data/words/word_clues/clues_four.json
/usr/lib64/R/library/rcorpora/corpora/data/words/word_clues/clues_six.json
/usr/lib64/R/library/rcorpora/corpora/package.json
/usr/lib64/R/library/rcorpora/help/AnIndex
/usr/lib64/R/library/rcorpora/help/aliases.rds
/usr/lib64/R/library/rcorpora/help/paths.rds
/usr/lib64/R/library/rcorpora/help/rcorpora.rdb
/usr/lib64/R/library/rcorpora/help/rcorpora.rdx
/usr/lib64/R/library/rcorpora/html/00Index.html
/usr/lib64/R/library/rcorpora/html/R.css
