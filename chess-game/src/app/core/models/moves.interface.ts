export interface Moves { 
    b1: Move[] | null,
    a1: Move[] | null,
    c1: Move[] | null,
    d1: Move[] | null,
    e1: Move[] | null,
    f1: Move[] | null,
    g1: Move[] | null,
    h1: Move[] | null,
    a2: Move[] | null,
    b2: Move[] | null,
    c2: Move[] | null,
    d2: Move[] | null,
    e2: Move[] | null,
    f2: Move[] | null,
    g2: Move[] | null,
    h2: Move[] | null,
    a3: Move[] | null,
    b3: Move[] | null,
    c3: Move[] | null,
    d3: Move[] | null,
    e3: Move[] | null,
    f3: Move[] | null,
    g3: Move[] | null,
    h3: Move[] | null,
    a4: Move[] | null,
    b4: Move[] | null,
    c4: Move[] | null,
    d4: Move[] | null,
    e4: Move[] | null,
    f4: Move[] | null,
    g4: Move[] | null,
    h4: Move[] | null,
    a5: Move[] | null,
    b5: Move[] | null,
    c5: Move[] | null,
    d5: Move[] | null,
    e5: Move[] | null,
    f5: Move[] | null,
    g5: Move[] | null,
    h5: Move[] | null,
    a6: Move[] | null,
    b6: Move[] | null,
    c6: Move[] | null,
    d6: Move[] | null,
    e6: Move[] | null,
    f6: Move[] | null,
    g6: Move[] | null,
    h6: Move[] | null,
    a7: Move[] | null,
    b7: Move[] | null,
    c7: Move[] | null,
    d7: Move[] | null,
    e7: Move[] | null,
    f7: Move[] | null,
    g7: Move[] | null,
    h7: Move[] | null,
    a8: Move[] | null,
    b8: Move[] | null,
    c8: Move[] | null,
    d8: Move[] | null,
    e8: Move[] | null,
    f8: Move[] | null,
    g8: Move[] | null,
    h8: Move[] | null,
}

export interface Move { 
    newPosition: string,
    isKill: boolean
}