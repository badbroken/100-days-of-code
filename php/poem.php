<?php
function generateStory ($singular_noun,$verb,$color,$distance_unit){
  $story =" The $singular_noun are lovely, $color, and deep. \nBut I have promises to keep, \n And $distance_unit to go before I $verb, \n And $distance_unit to go before I $verb.";

  return $story;
}

echo generateStory("woods","sleep","dark","Miles");