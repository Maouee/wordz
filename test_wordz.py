import wordz


def test_compte_mots() : 
    counts = wordz.compte_mots(["À l'âge de 12 ans, Dave Grohl apprend la guitare. Après s'être lassé des leçons de guitare, Grohl apprend lui-même."])
    assert counts["guitare"] == 2
    assert counts["Grohl"] == 1
    assert counts["titicaca"] == 0 
    assert counts["ans,"] == 0