module Echidna.Types.Corpus where

import Data.Set (Set, size)
import Echidna.Types.Tx (Tx)

type Corpus = Set (Hash, [Tx])

type Hash = Int

corpusSize :: Corpus -> Int
corpusSize = size
