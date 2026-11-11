"""9 PRI saung symbols, derived from the meaning of each saung name.
Single colour, round caps, 120x120 viewBox, stroke drawn with currentColor."""

S = 'fill="none" stroke="currentColor" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"'

GLYPHS = {
    # honje / torch ginger: tall stem, layered pointed bracts forming a torch
    'Cihonje': ('Kecombrang, bunga rempah', '''
<path d="M60 112 V70"/>
<path d="M60 70 C42 66 36 50 40 36 C46 46 54 56 60 70 Z"/>
<path d="M60 70 C78 66 84 50 80 36 C74 46 66 56 60 70 Z"/>
<path d="M60 64 C50 52 50 30 60 12 C70 30 70 52 60 64 Z"/>
<path d="M54 46 L60 40 L66 46 M55 32 L60 27 L65 32"/>
<path d="M60 98 C44 98 30 92 22 80 M60 92 C76 92 90 86 98 74"/>'''),
    # tengah: a stone in the middle of the stream
    'Citengah': ('Batu di tengah aliran sungai', '''
<path d="M12 40 q12 -8 24 0 t24 0 t24 0 t24 0"/>
<path d="M12 84 q12 -8 24 0 t24 0 t24 0 t24 0"/>
<ellipse cx="60" cy="62" rx="16" ry="10"/>'''),
    # soka / ixora: a dome cluster of small four-petal flowers
    'Cisoka': ('Bunga soka bergerombol', '''<circle cx="64.2" cy="24.0" r="3.2"/><circle cx="60.0" cy="28.2" r="3.2"/><circle cx="55.8" cy="24.0" r="3.2"/><circle cx="60.0" cy="19.8" r="3.2"/><circle cx="49.2" cy="32.0" r="3.2"/><circle cx="45.0" cy="36.2" r="3.2"/><circle cx="40.8" cy="32.0" r="3.2"/><circle cx="45.0" cy="27.8" r="3.2"/><circle cx="79.2" cy="32.0" r="3.2"/><circle cx="75.0" cy="36.2" r="3.2"/><circle cx="70.8" cy="32.0" r="3.2"/><circle cx="75.0" cy="27.8" r="3.2"/><circle cx="38.2" cy="46.0" r="3.2"/><circle cx="34.0" cy="50.2" r="3.2"/><circle cx="29.8" cy="46.0" r="3.2"/><circle cx="34.0" cy="41.8" r="3.2"/><circle cx="56.2" cy="44.0" r="3.2"/><circle cx="52.0" cy="48.2" r="3.2"/><circle cx="47.8" cy="44.0" r="3.2"/><circle cx="52.0" cy="39.8" r="3.2"/><circle cx="72.2" cy="44.0" r="3.2"/><circle cx="68.0" cy="48.2" r="3.2"/><circle cx="63.8" cy="44.0" r="3.2"/><circle cx="68.0" cy="39.8" r="3.2"/><circle cx="90.2" cy="46.0" r="3.2"/><circle cx="86.0" cy="50.2" r="3.2"/><circle cx="81.8" cy="46.0" r="3.2"/><circle cx="86.0" cy="41.8" r="3.2"/><circle cx="48.2" cy="58.0" r="3.2"/><circle cx="44.0" cy="62.2" r="3.2"/><circle cx="39.8" cy="58.0" r="3.2"/><circle cx="44.0" cy="53.8" r="3.2"/><circle cx="64.2" cy="57.0" r="3.2"/><circle cx="60.0" cy="61.2" r="3.2"/><circle cx="55.8" cy="57.0" r="3.2"/><circle cx="60.0" cy="52.8" r="3.2"/><circle cx="80.2" cy="58.0" r="3.2"/><circle cx="76.0" cy="62.2" r="3.2"/><circle cx="71.8" cy="58.0" r="3.2"/><circle cx="76.0" cy="53.8" r="3.2"/>
<path d="M60 70 V112"/>
<path d="M60 96 C46 98 34 92 28 80 C42 78 54 84 60 96 Z"/>
<path d="M60 88 C74 90 86 84 92 72 C78 70 66 76 60 88 Z"/>'''),
    # tundun / mountain rambutan: hairy round fruits hanging from a twig
    'Citundun': ('Rambutan gunung', '''
<path d="M18 18 C40 14 58 18 70 30"/>
<path d="M44 18 C40 30 40 40 42 50 M70 30 C76 40 78 50 78 60"/>
<path d="M30 16 C30 6 40 2 50 4 C46 12 38 16 30 16 Z"/><circle cx="42" cy="70" r="16"/><path d="M60.0 70.0 Q63.8 66.7 65.3 75.9 M58.2 77.8 Q63.0 76.5 60.4 85.4 M53.2 84.1 Q58.1 85.0 51.9 91.9 M46.0 87.5 Q50.0 90.5 41.4 94.0 M38.0 87.5 Q40.4 91.9 31.0 91.3 M30.8 84.1 Q31.0 89.1 22.9 84.5 M25.8 77.8 Q23.8 82.4 18.5 74.7 M24.0 70.0 Q20.2 73.3 18.7 64.1 M25.8 62.2 Q21.0 63.5 23.6 54.6 M30.8 55.9 Q25.9 55.0 32.1 48.1 M38.0 52.5 Q34.0 49.5 42.6 46.0 M46.0 52.5 Q43.6 48.1 53.0 48.7 M53.2 55.9 Q53.0 50.9 61.1 55.5 M58.2 62.2 Q60.2 57.6 65.5 65.3 "/><circle cx="80" cy="80" r="12"/><path d="M94.0 80.0 Q97.8 77.3 99.4 84.9 M91.8 87.6 Q96.4 87.4 93.6 94.6 M85.8 92.7 Q89.8 95.1 83.5 99.7 M78.0 93.9 Q80.1 98.0 72.3 98.5 M70.8 90.6 Q70.4 95.2 63.6 91.4 M66.6 83.9 Q63.7 87.6 60.0 80.7 M66.6 76.1 Q62.2 77.6 62.8 69.8 M70.8 69.4 Q66.3 68.3 71.0 62.1 M78.0 66.1 Q74.8 62.8 82.1 60.1 M85.8 67.3 Q84.9 62.7 92.6 64.4 M91.8 72.4 Q93.5 68.1 99.0 73.7 "/>'''),
    # ambu / mother (Sunan Ambu in kahyangan): sheltering arc over a crescent
    'Ambu': ('Ibu, Sunan Ambu di kahyangan', '''
<path d="M14 100 C14 52 34 22 60 22 C86 22 106 52 106 100"/>
<path d="M30 100 C30 66 42 44 60 40"/>
<path d="M90 100 C90 66 78 44 60 40"/>
<path d="M66 86 A16 16 0 1 1 66 54 A12 12 0 1 0 66 86 Z"/>'''),
    # indung / mother, source, spring: water rising from the ground, ripples
    'Indung': ('Ibu, asal, mata air', '''
<path d="M60 16 C70 32 78 42 78 54 A18 18 0 0 1 42 54 C42 42 50 32 60 16 Z"/>
<path d="M52 56 A9 9 0 0 0 60 64"/>
<path d="M32 88 C40 82 80 82 88 88 C80 94 40 94 32 88 Z"/>
<path d="M14 92 C26 102 94 102 106 92"/>'''),
    # jolang: a trough carved from a tree trunk, holding water
    'Cijolang': ('Palung dari batang kayu', '''
<ellipse cx="22" cy="58" rx="10" ry="16"/>
<ellipse cx="22" cy="58" rx="5" ry="8"/>
<path d="M22 42 H96 C106 42 110 50 110 58 C110 66 106 74 96 74 H22"/>
<path d="M34 50 H96 C100 50 102 54 102 58 C102 62 100 66 96 66 H34"/>
<path d="M44 58 q6 -4 12 0 t12 0 t12 0 t12 0"/>
<path d="M40 84 H100 M54 92 H92"/>'''),
    # karut: an earthen jar wrapped in a net of rope
    'Cikarut': ('Tempayan berlilit tali', '''
<path d="M48 16 H72"/>
<path d="M50 16 V24 C30 32 22 50 24 68 C26 90 42 104 60 104 C78 104 94 90 96 68 C98 50 90 32 70 24 V16"/>
<path d="M30 42 C48 50 72 50 90 42"/>
<path d="M24 64 C46 74 74 74 96 64"/>
<path d="M30 88 C48 96 72 96 90 88"/>
<path d="M44 46 C40 60 40 80 46 98 M60 48 V102 M76 46 C80 60 80 80 74 98"/>'''),
    # dewa: the largest saung, a julang ngapak roof with a halo above
    'Dewa': ('Saung terbesar', '''
<path d="M50 14 L62 34 M70 14 L58 34"/>
<path d="M6 72 C30 68 46 54 60 30 C74 54 90 68 114 72"/>
<path d="M22 72 C36 66 48 56 60 44 C72 56 84 66 98 72"/>
<path d="M26 72 V100 M94 72 V100 M12 100 H108"/>
<path d="M48 100 V82 H72 V100"/>'''),
}

ORDER = ['Cihonje', 'Citengah', 'Cisoka', 'Citundun', 'Ambu', 'Indung', 'Cijolang', 'Cikarut', 'Dewa']


def svg(name, size=120, w=3, color=None):
    style = f' style="color:{color}"' if color else ''
    return (f'<svg viewBox="0 0 120 120" width="{size}" height="{size}"{style} '
            f'xmlns="http://www.w3.org/2000/svg"><g {S.format(w=w)}>{GLYPHS[name][1]}</g></svg>')


def meaning(name):
    return GLYPHS[name][0]
