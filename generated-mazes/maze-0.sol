pragma solidity ^0.8.19;
/// automatically generated by Daedaluzz
contract Maze {
  event AssertionFailed(string message);
  bool private echidna_flag_1 = true;
  bool private echidna_flag_2 = true;
  bool private echidna_flag_3 = true;
  bool private echidna_flag_4 = true;
  bool private echidna_flag_5 = true;
  bool private echidna_flag_6 = true;
  bool private echidna_flag_7 = true;
  bool private echidna_flag_8 = true;
  bool private echidna_flag_9 = true;
  bool private echidna_flag_10 = true;
  bool private echidna_flag_11 = true;
  bool private echidna_flag_12 = true;
  bool private echidna_flag_13 = true;
  bool private echidna_flag_14 = true;
  bool private echidna_flag_15 = true;
  bool private echidna_flag_16 = true;
  bool private echidna_flag_17 = true;
  bool private echidna_flag_18 = true;
  bool private echidna_flag_19 = true;
  bool private echidna_flag_20 = true;
  bool private echidna_flag_21 = true;
  bool private echidna_flag_22 = true;
  bool private echidna_flag_23 = true;
  bool private echidna_flag_24 = true;
  bool private echidna_flag_25 = true;
  bool private echidna_flag_26 = true;
  bool private echidna_flag_27 = true;
  bool private echidna_flag_28 = true;
  bool private echidna_flag_29 = true;
  bool private echidna_flag_30 = true;
  bool private echidna_flag_31 = true;
  bool private echidna_flag_32 = true;
  bool private echidna_flag_33 = true;
  bool private echidna_flag_34 = true;
  bool private echidna_flag_35 = true;
  bool private echidna_flag_36 = true;
  bool private echidna_flag_37 = true;
  bool private echidna_flag_38 = true;
  bool private echidna_flag_39 = true;
  bool private echidna_flag_40 = true;
  bool private echidna_flag_41 = true;
  bool private echidna_flag_42 = true;
  bool private echidna_flag_43 = true;
  bool private echidna_flag_44 = true;
  bool private echidna_flag_45 = true;
  bool private echidna_flag_46 = true;
  bool private echidna_flag_47 = true;

  uint64 private x;
  uint64 private y;
  function moveNorth(uint64 p0, uint64 p1, uint64 p2, uint64 p3, uint64 p4, uint64 p5, uint64 p6, uint64 p7) payable external returns (int64) {
    uint64 ny = y + 1;
    require(ny < 7);
    y = ny;
    return step(p0, p1, p2, p3, p4, p5, p6, p7);
  }
  function moveSouth(uint64 p0, uint64 p1, uint64 p2, uint64 p3, uint64 p4, uint64 p5, uint64 p6, uint64 p7) payable external returns (int64) {
    require(0 < y);
    uint64 ny = y - 1;
    y = ny;
    return step(p0, p1, p2, p3, p4, p5, p6, p7);
  }
  function moveEast(uint64 p0, uint64 p1, uint64 p2, uint64 p3, uint64 p4, uint64 p5, uint64 p6, uint64 p7) payable external returns (int64) {
    uint64 nx = x + 1;
    require(nx < 7);
    x = nx;
    return step(p0, p1, p2, p3, p4, p5, p6, p7);
  }
  function moveWest(uint64 p0, uint64 p1, uint64 p2, uint64 p3, uint64 p4, uint64 p5, uint64 p6, uint64 p7) payable external returns (int64) {
    require(0 < x);
    uint64 nx = x - 1;
    x = nx;
    return step(p0, p1, p2, p3, p4, p5, p6, p7);
  }
  function step(uint64 p0, uint64 p1, uint64 p2, uint64 p3, uint64 p4, uint64 p5, uint64 p6, uint64 p7) internal returns (int64) {
    unchecked {
      if (x == 0 && y == 0) {
        // start
        return 0;
      }
      if (x == 0 && y == 1) {
        if (p2 != p2) {
          if (p0 < p5) {
            if (p0 != uint64(46)) {
              if (p4 != uint64(27)) {
                if (p2 < uint64(uint64(61) * p3)) {
                  if (p2 < uint64(49)) {
                    echidna_flag_1 = false;
                  }
                }
              }
            }
          }
        }
        return 1;
      }
      if (x == 0 && y == 2) {
        if (p0 >= p4) {
          if (p4 > uint64(p4 * p6)) {
            if (p0 > uint64(uint64(27) * p2)) {
              if (p4 > uint64(20)) {
                if (p7 < uint64(49)) {
                  if (p1 == uint64(uint64(7) + p2)) {
                    if (p3 <= uint64(33)) {
                      if (p4 >= uint64(uint64(22) + p3)) {
                        if (p2 <= uint64(uint64(12) * p7)) {
                          if (p1 < p7) {
                            if (p4 > uint64(p2 + p5)) {
                              echidna_flag_2 = false;
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 2;
      }
      if (x == 0 && y == 3) {
        if (p7 <= uint64(p6 + p6)) {
          if (p3 <= uint64(uint64(64) * p2)) {
            if (p4 <= uint64(34)) {
              if (p0 >= uint64(uint64(28) * p2)) {
                if (p4 > uint64(37)) {
                  if (p5 >= uint64(p5 * p6)) {
                    if (p7 == uint64(uint64(20) * p6)) {
                      if (p2 >= uint64(48)) {
                        if (p3 >= uint64(p0 + p0)) {
                          if (p3 <= uint64(4)) {
                            if (p7 < uint64(p7 + p5)) {
                              if (p1 != uint64(58)) {
                                if (p4 >= uint64(47)) {
                                  echidna_flag_3 = false;
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 3;
      }
      if (x == 0 && y == 4) {
        if (p2 != uint64(37)) {
          if (p1 <= uint64(p1 + p5)) {
            if (p1 > uint64(2)) {
              if (p0 == uint64(uint64(13) * p3)) {
                if (p2 == uint64(p2 * p7)) {
                  if (p4 == uint64(28)) {
                    if (p3 > uint64(31)) {
                      if (p4 < uint64(uint64(40) * p4)) {
                        echidna_flag_4 = false;
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 4;
      }
      if (x == 0 && y == 5) {
        if (p6 != uint64(uint64(2) + p1)) {
          if (p4 == uint64(p5 * p5)) {
            echidna_flag_5 = false;
          }
        }
        return 5;
      }
      if (x == 0 && y == 6) {
        if (p6 >= uint64(uint64(39) * p5)) {
          if (p4 >= uint64(uint64(55) * p4)) {
            if (p4 <= uint64(p6 * p6)) {
              if (p2 == uint64(uint64(12) + p4)) {
                if (p0 <= uint64(uint64(18) * p2)) {
                  if (p1 >= uint64(57)) {
                    if (p6 >= uint64(41)) {
                      echidna_flag_6 = false;
                    }
                  }
                }
              }
            }
          }
        }
        return 6;
      }
      if (x == 1 && y == 0) {
        require(false);  // wall
        return 7;
      }
      if (x == 1 && y == 1) {
        if (p7 <= uint64(p6 + p5)) {
          if (p0 >= uint64(uint64(62) + p2)) {
            if (p2 == uint64(p3 * p3)) {
              if (p0 >= uint64(24)) {
                if (p2 >= uint64(p7 + p6)) {
                  if (p1 >= p2) {
                    if (p1 == uint64(p4 * p3)) {
                      if (p0 < uint64(uint64(54) * p2)) {
                        echidna_flag_8 = false;
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 8;
      }
      if (x == 1 && y == 2) {
        if (p0 < p4) {
          if (p7 <= p7) {
            if (p0 < uint64(p0 * p4)) {
              if (p7 >= uint64(p2 + p1)) {
                if (p6 >= p6) {
                  if (p4 > uint64(p7 * p4)) {
                    if (p3 < uint64(29)) {
                      echidna_flag_9 = false;
                    }
                  }
                }
              }
            }
          }
        }
        return 9;
      }
      if (x == 1 && y == 3) {
        if (p3 != uint64(41)) {
          if (p7 == uint64(uint64(46) + p4)) {
            if (p6 == p1) {
              if (p3 >= uint64(p4 * p6)) {
                if (p5 < uint64(p7 * p5)) {
                  if (p4 == p3) {
                    if (p5 > uint64(p4 + p3)) {
                      if (p3 != uint64(uint64(53) + p6)) {
                        if (p5 >= uint64(p2 * p7)) {
                          if (p2 == uint64(21)) {
                            if (p6 > uint64(uint64(43) * p3)) {
                              if (p1 == uint64(p7 * p4)) {
                                if (p5 <= uint64(uint64(8) * p0)) {
                                  if (p7 > uint64(17)) {
                                    if (p4 < uint64(p7 * p1)) {
                                      if (p5 > uint64(p1 * p0)) {
                                        echidna_flag_10 = false;
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 10;
      }
      if (x == 1 && y == 4) {
        if (p6 < uint64(p2 * p6)) {
          if (p3 == uint64(p3 * p2)) {
            if (p2 != uint64(p4 * p4)) {
              if (p3 > uint64(uint64(61) + p4)) {
                if (p7 > uint64(p7 * p4)) {
                  if (p1 < uint64(uint64(9) * p0)) {
                    if (p1 != uint64(p2 * p7)) {
                      echidna_flag_11 = false;
                    }
                  }
                }
              }
            }
          }
        }
        return 11;
      }
      if (x == 1 && y == 5) {
        require(false);  // wall
        return 12;
      }
      if (x == 1 && y == 6) {
        if (p0 <= uint64(uint64(51) + p3)) {
          if (p4 != uint64(uint64(31) + p7)) {
            if (p5 < uint64(p2 * p4)) {
              if (p0 > uint64(46)) {
                if (p6 == uint64(11)) {
                  if (p0 == uint64(50)) {
                    if (p3 <= p0) {
                      if (p5 < uint64(41)) {
                        echidna_flag_13 = false;
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 13;
      }
      if (x == 2 && y == 0) {
        if (p5 >= p2) {
          if (p3 <= uint64(p0 * p4)) {
            if (p2 > p2) {
              if (p7 <= uint64(p0 + p6)) {
                if (p6 <= uint64(uint64(26) + p1)) {
                  if (p6 != uint64(uint64(21) * p6)) {
                    if (p5 != uint64(uint64(42) * p0)) {
                      if (p1 < uint64(p6 + p1)) {
                        if (p1 <= uint64(25)) {
                          if (p5 <= uint64(uint64(0) * p6)) {
                            if (p3 == uint64(p2 + p2)) {
                              if (p3 < p7) {
                                echidna_flag_14 = false;
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 14;
      }
      if (x == 2 && y == 1) {
        if (p3 != uint64(6)) {
          if (p3 < p3) {
            if (p3 < uint64(p4 + p7)) {
              if (p5 < uint64(p1 + p7)) {
                if (p4 > uint64(uint64(21) + p0)) {
                  if (p0 <= uint64(uint64(60) + p0)) {
                    if (p7 < uint64(uint64(39) * p3)) {
                      if (p2 <= uint64(19)) {
                        if (p7 != uint64(uint64(26) + p0)) {
                          if (p4 > uint64(15)) {
                            if (p0 != uint64(uint64(47) + p1)) {
                              if (p2 != uint64(p2 + p0)) {
                                if (p6 >= uint64(p5 + p6)) {
                                  if (p0 == uint64(p0 * p2)) {
                                    if (p6 < uint64(31)) {
                                      if (p4 <= uint64(p7 * p5)) {
                                        echidna_flag_15 = false;
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 15;
      }
      if (x == 2 && y == 2) {
        if (p5 != uint64(10)) {
          if (p5 != p0) {
            if (p4 >= uint64(p2 * p1)) {
              if (p3 > uint64(uint64(31) + p5)) {
                echidna_flag_16 = false;
              }
            }
          }
        }
        return 16;
      }
      if (x == 2 && y == 3) {
        if (p6 == uint64(10)) {
          if (p5 == uint64(uint64(50) * p5)) {
            if (p0 > uint64(17)) {
              echidna_flag_17 = false;
            }
          }
        }
        return 17;
      }
      if (x == 2 && y == 4) {
        if (p5 >= uint64(p5 * p7)) {
          if (p0 < p1) {
            if (p2 == uint64(p3 + p7)) {
              echidna_flag_18 = false;
            }
          }
        }
        return 18;
      }
      if (x == 2 && y == 5) {
        if (p4 > p2) {
          if (p6 > uint64(40)) {
            if (p1 != uint64(p1 * p1)) {
              if (p4 > uint64(p7 + p5)) {
                echidna_flag_19 = false;
              }
            }
          }
        }
        return 19;
      }
      if (x == 2 && y == 6) {
        require(false);  // wall
        return 20;
      }
      if (x == 3 && y == 0) {
        if (p3 > uint64(uint64(3) * p0)) {
          if (p1 != uint64(13)) {
            if (p1 > uint64(45)) {
              if (p5 > uint64(uint64(39) + p0)) {
                if (p7 == uint64(p2 + p0)) {
                  if (p4 >= uint64(uint64(16) * p1)) {
                    if (p4 == uint64(38)) {
                      if (p0 >= uint64(uint64(52) * p0)) {
                        if (p2 == uint64(p6 * p5)) {
                          if (p2 < uint64(uint64(2) + p1)) {
                            if (p1 <= p1) {
                              if (p2 > p7) {
                                echidna_flag_21 = false;
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 21;
      }
      if (x == 3 && y == 1) {
        require(false);  // wall
        return 22;
      }
      if (x == 3 && y == 2) {
        if (p3 > uint64(p0 + p6)) {
          if (p5 != uint64(p6 + p4)) {
            if (p2 >= uint64(p0 + p6)) {
              if (p4 != uint64(p1 * p6)) {
                if (p6 > uint64(p3 + p4)) {
                  if (p4 > uint64(uint64(29) * p2)) {
                    if (p7 != uint64(p0 + p7)) {
                      if (p3 != uint64(p6 * p5)) {
                        if (p4 != uint64(p3 * p1)) {
                          if (p0 == uint64(55)) {
                            if (p2 >= uint64(uint64(23) * p5)) {
                              if (p1 <= p1) {
                                if (p2 > uint64(p4 * p7)) {
                                  if (p1 <= uint64(uint64(45) * p5)) {
                                    if (p4 > uint64(p7 + p7)) {
                                      if (p3 > uint64(uint64(54) * p4)) {
                                        echidna_flag_23 = false;
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 23;
      }
      if (x == 3 && y == 3) {
        if (p0 > p2) {
          if (p6 != p6) {
            if (p5 != uint64(p2 + p2)) {
              echidna_flag_24 = false;
            }
          }
        }
        return 24;
      }
      if (x == 3 && y == 4) {
        if (p2 >= uint64(34)) {
          if (p3 <= uint64(9)) {
            if (p1 >= uint64(p2 * p4)) {
              if (p1 == p7) {
                if (p0 > uint64(uint64(57) + p6)) {
                  if (p1 <= uint64(uint64(53) + p4)) {
                    if (p2 >= uint64(uint64(25) * p0)) {
                      if (p6 < uint64(p5 + p6)) {
                        if (p3 >= uint64(uint64(48) * p6)) {
                          if (p7 <= uint64(uint64(23) + p3)) {
                            echidna_flag_25 = false;
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 25;
      }
      if (x == 3 && y == 5) {
        if (p0 > uint64(p1 + p7)) {
          if (p0 == p7) {
            if (p2 != uint64(p6 + p4)) {
              if (p4 >= uint64(47)) {
                if (p5 >= uint64(p5 + p4)) {
                  if (p3 != uint64(28)) {
                    if (p7 == uint64(36)) {
                      if (p5 > uint64(p4 * p4)) {
                        echidna_flag_26 = false;
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 26;
      }
      if (x == 3 && y == 6) {
        if (p7 < uint64(1)) {
          if (p1 > uint64(uint64(8) * p6)) {
            if (p7 <= uint64(uint64(31) * p6)) {
              echidna_flag_27 = false;
            }
          }
        }
        return 27;
      }
      if (x == 4 && y == 0) {
        if (p3 >= uint64(uint64(9) * p7)) {
          if (p5 < uint64(8)) {
            if (p4 != p1) {
              if (p6 >= uint64(uint64(3) * p2)) {
                if (p0 >= uint64(p5 + p3)) {
                  if (p2 < uint64(uint64(63) + p7)) {
                    if (p6 <= uint64(uint64(3) * p4)) {
                      if (p2 <= uint64(46)) {
                        if (p0 != uint64(uint64(42) * p1)) {
                          if (p1 == p5) {
                            echidna_flag_28 = false;
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 28;
      }
      if (x == 4 && y == 1) {
        if (p1 > uint64(63)) {
          if (p0 == uint64(uint64(35) * p2)) {
            if (p0 != uint64(p2 * p6)) {
              echidna_flag_29 = false;
            }
          }
        }
        return 29;
      }
      if (x == 4 && y == 2) {
        if (p4 <= uint64(uint64(31) * p4)) {
          if (p5 < uint64(p5 * p5)) {
            if (p5 > uint64(uint64(41) + p6)) {
              if (p3 >= uint64(uint64(45) + p4)) {
                if (p6 <= uint64(uint64(8) * p7)) {
                  if (p0 < uint64(6)) {
                    if (p2 == uint64(p0 * p3)) {
                      echidna_flag_30 = false;
                    }
                  }
                }
              }
            }
          }
        }
        return 30;
      }
      if (x == 4 && y == 3) {
        if (p0 == uint64(uint64(49) + p5)) {
          if (p2 >= uint64(30)) {
            if (p6 > uint64(uint64(50) * p0)) {
              if (p3 <= uint64(uint64(13) * p1)) {
                if (p5 > uint64(p6 + p2)) {
                  if (p1 <= p5) {
                    if (p4 <= p5) {
                      if (p5 > uint64(uint64(49) * p7)) {
                        if (p2 > uint64(p4 * p3)) {
                          if (p4 != uint64(33)) {
                            if (p2 != uint64(uint64(14) + p5)) {
                              if (p5 <= uint64(25)) {
                                if (p4 < uint64(uint64(52) + p5)) {
                                  if (p1 >= p2) {
                                    echidna_flag_31 = false;
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 31;
      }
      if (x == 4 && y == 4) {
        if (p2 > uint64(39)) {
          if (p2 >= uint64(p5 + p1)) {
            if (p6 >= uint64(p2 * p6)) {
              if (p7 > uint64(5)) {
                if (p0 == uint64(34)) {
                  if (p1 >= uint64(uint64(56) + p3)) {
                    if (p3 == p4) {
                      if (p2 > uint64(uint64(4) * p1)) {
                        if (p2 <= uint64(18)) {
                          if (p5 == uint64(uint64(10) + p0)) {
                            if (p7 <= uint64(p0 * p2)) {
                              if (p3 < uint64(p4 * p7)) {
                                if (p6 == uint64(42)) {
                                  if (p3 < uint64(p6 * p7)) {
                                    if (p5 != uint64(p1 * p2)) {
                                      echidna_flag_32 = false;
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 32;
      }
      if (x == 4 && y == 5) {
        if (p7 <= p4) {
          if (p4 >= uint64(p7 * p6)) {
            if (p5 <= p6) {
              if (p4 <= p1) {
                if (p2 != uint64(p2 * p7)) {
                  if (p0 <= uint64(p4 * p0)) {
                    if (p6 <= p1) {
                      if (p0 < uint64(p6 + p1)) {
                        if (p7 <= p7) {
                          if (p0 >= uint64(uint64(61) * p4)) {
                            if (p2 < uint64(p0 * p3)) {
                              if (p1 == p0) {
                                if (p3 == uint64(uint64(59) * p0)) {
                                  if (p3 <= uint64(uint64(16) + p6)) {
                                    if (p4 == uint64(p2 * p1)) {
                                      if (p7 < uint64(5)) {
                                        echidna_flag_33 = false;
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 33;
      }
      if (x == 4 && y == 6) {
        if (p4 <= uint64(uint64(4) + p1)) {
          if (p6 < uint64(uint64(63) + p3)) {
            if (p5 >= uint64(uint64(30) * p5)) {
              if (p2 != uint64(uint64(27) * p6)) {
                echidna_flag_34 = false;
              }
            }
          }
        }
        return 34;
      }
      if (x == 5 && y == 0) {
        if (p3 >= uint64(55)) {
          if (p4 >= uint64(uint64(52) * p2)) {
            if (p0 != uint64(uint64(56) * p1)) {
              echidna_flag_35 = false;
            }
          }
        }
        return 35;
      }
      if (x == 5 && y == 1) {
        if (p1 > p6) {
          if (p7 < uint64(uint64(34) * p4)) {
            if (p2 == p1) {
              if (p7 >= uint64(32)) {
                if (p1 == uint64(uint64(38) * p1)) {
                  if (p0 > uint64(uint64(52) * p7)) {
                    if (p0 > uint64(uint64(38) + p5)) {
                      if (p3 > uint64(64)) {
                        if (p3 > p6) {
                          if (p3 == p0) {
                            if (p1 > uint64(42)) {
                              if (p6 <= p3) {
                                if (p3 != uint64(uint64(55) * p0)) {
                                  echidna_flag_36 = false;
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 36;
      }
      if (x == 5 && y == 2) {
        if (p4 == uint64(26)) {
          if (p7 < p4) {
            if (p6 > p2) {
              if (p6 > p5) {
                if (p2 > uint64(p0 * p2)) {
                  if (p3 >= uint64(p5 + p7)) {
                    if (p6 < p3) {
                      if (p7 < uint64(46)) {
                        if (p2 < uint64(uint64(44) * p1)) {
                          if (p7 != p0) {
                            if (p5 != uint64(35)) {
                              if (p6 != uint64(p2 + p2)) {
                                echidna_flag_37 = false;
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 37;
      }
      if (x == 5 && y == 3) {
        if (p2 >= uint64(uint64(6) * p4)) {
          if (p5 <= uint64(uint64(6) + p1)) {
            if (p4 <= p6) {
              if (p5 < uint64(p5 * p2)) {
                if (p2 >= p4) {
                  if (p3 == uint64(43)) {
                    if (p4 <= uint64(uint64(49) + p6)) {
                      if (p3 <= uint64(p0 * p3)) {
                        if (p3 != uint64(uint64(28) + p7)) {
                          if (p2 < uint64(uint64(20) * p1)) {
                            if (p2 != p6) {
                              echidna_flag_38 = false;
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 38;
      }
      if (x == 5 && y == 4) {
        if (p5 < uint64(uint64(59) * p6)) {
          if (p5 <= uint64(32)) {
            if (p3 < uint64(p4 + p1)) {
              if (p5 == uint64(31)) {
                if (p7 == uint64(uint64(36) * p1)) {
                  echidna_flag_39 = false;
                }
              }
            }
          }
        }
        return 39;
      }
      if (x == 5 && y == 5) {
        if (p5 > uint64(uint64(41) + p3)) {
          if (p4 >= p5) {
            if (p6 == uint64(uint64(25) + p5)) {
              if (p0 > uint64(p5 * p3)) {
                if (p7 == uint64(7)) {
                  if (p3 >= uint64(19)) {
                    if (p5 <= uint64(uint64(61) * p5)) {
                      if (p7 < p1) {
                        if (p2 <= p3) {
                          echidna_flag_40 = false;
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 40;
      }
      if (x == 5 && y == 6) {
        if (p7 != uint64(p2 + p3)) {
          if (p2 < uint64(60)) {
            if (p0 < uint64(p4 + p0)) {
              if (p3 != uint64(p4 * p0)) {
                if (p1 <= uint64(33)) {
                  if (p1 >= uint64(p6 + p6)) {
                    if (p4 <= uint64(p2 + p0)) {
                      if (p5 <= uint64(uint64(47) * p7)) {
                        if (p5 != uint64(uint64(12) + p6)) {
                          if (p5 >= uint64(uint64(52) * p2)) {
                            if (p0 <= uint64(p2 * p5)) {
                              if (p3 >= p7) {
                                if (p2 == p4) {
                                  echidna_flag_41 = false;
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 41;
      }
      if (x == 6 && y == 0) {
        if (p4 >= uint64(uint64(34) + p7)) {
          if (p4 != uint64(p7 + p2)) {
            if (p7 <= uint64(p7 * p3)) {
              echidna_flag_42 = false;
            }
          }
        }
        return 42;
      }
      if (x == 6 && y == 1) {
        if (p2 == uint64(p4 + p1)) {
          if (p5 == uint64(uint64(12) + p3)) {
            if (p7 >= uint64(p5 * p3)) {
              echidna_flag_43 = false;
            }
          }
        }
        return 43;
      }
      if (x == 6 && y == 2) {
        if (p5 == uint64(uint64(3) + p5)) {
          if (p0 != uint64(p0 * p1)) {
            echidna_flag_44 = false;
          }
        }
        return 44;
      }
      if (x == 6 && y == 3) {
        if (p0 < uint64(23)) {
          if (p2 >= p0) {
            if (p3 < uint64(uint64(50) * p2)) {
              if (p4 > uint64(p3 + p1)) {
                if (p7 >= uint64(uint64(52) * p5)) {
                  if (p6 <= uint64(p1 * p6)) {
                    if (p1 > uint64(p3 + p7)) {
                      if (p6 < uint64(p5 + p1)) {
                        if (p0 > uint64(uint64(9) + p5)) {
                          if (p6 < p0) {
                            if (p1 > uint64(p0 + p2)) {
                              if (p3 <= uint64(p0 * p0)) {
                                if (p5 != p7) {
                                  if (p1 < uint64(p5 + p0)) {
                                    if (p6 == uint64(p7 + p5)) {
                                      echidna_flag_45 = false;
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 45;
      }
      if (x == 6 && y == 4) {
        if (p7 <= p1) {
          if (p5 < p2) {
            if (p2 != p3) {
              if (p0 > uint64(uint64(39) + p7)) {
                if (p3 <= uint64(p1 * p6)) {
                  if (p2 > uint64(34)) {
                    if (p4 == uint64(uint64(26) * p4)) {
                      if (p3 >= p2) {
                        if (p5 >= uint64(uint64(15) * p3)) {
                          if (p4 == uint64(p1 + p2)) {
                            if (p1 > uint64(uint64(0) + p5)) {
                              if (p4 <= uint64(p7 * p1)) {
                                if (p7 >= uint64(56)) {
                                  if (p4 > uint64(61)) {
                                    if (p7 > uint64(p1 * p6)) {
                                      echidna_flag_46 = false;
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 46;
      }
      if (x == 6 && y == 5) {
        if (p0 > uint64(18)) {
          if (p7 >= uint64(uint64(59) * p0)) {
            if (p0 >= uint64(37)) {
              if (p5 < uint64(uint64(44) * p3)) {
                if (p2 < uint64(p3 * p7)) {
                  if (p0 <= uint64(p3 * p6)) {
                    if (p7 <= p1) {
                      if (p7 >= uint64(uint64(8) + p5)) {
                        if (p5 < uint64(p5 * p3)) {
                          if (p3 < uint64(uint64(55) + p3)) {
                            if (p4 < uint64(41)) {
                              if (p0 >= uint64(uint64(53) + p7)) {
                                if (p4 > uint64(uint64(52) * p1)) {
                                  if (p2 == uint64(p0 + p7)) {
                                    if (p6 > uint64(p0 * p5)) {
                                      if (p6 <= uint64(p4 + p4)) {
                                        echidna_flag_47 = false;
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        return 47;
      }
      if (x == 6 && y == 6) {
        require(false);  // wall
        return 48;
      }
      return 49;
    }
  }

  function echidna_flag_1_property() public returns (bool) {
    return echidna_flag_1;
  }
  function echidna_flag_2_property() public returns (bool) {
    return echidna_flag_2;
  }
  function echidna_flag_3_property() public returns (bool) {
    return echidna_flag_3;
  }
  function echidna_flag_4_property() public returns (bool) {
    return echidna_flag_4;
  }
  function echidna_flag_5_property() public returns (bool) {
    return echidna_flag_5;
  }
  function echidna_flag_6_property() public returns (bool) {
    return echidna_flag_6;
  }
  function echidna_flag_7_property() public returns (bool) {
    return echidna_flag_7;
  }
  function echidna_flag_8_property() public returns (bool) {
    return echidna_flag_8;
  }
  function echidna_flag_9_property() public returns (bool) {
    return echidna_flag_9;
  }
  function echidna_flag_10_property() public returns (bool) {
    return echidna_flag_10;
  }
  function echidna_flag_11_property() public returns (bool) {
    return echidna_flag_11;
  }
  function echidna_flag_12_property() public returns (bool) {
    return echidna_flag_12;
  }
  function echidna_flag_13_property() public returns (bool) {
    return echidna_flag_13;
  }
  function echidna_flag_14_property() public returns (bool) {
    return echidna_flag_14;
  }
  function echidna_flag_15_property() public returns (bool) {
    return echidna_flag_15;
  }
  function echidna_flag_16_property() public returns (bool) {
    return echidna_flag_16;
  }
  function echidna_flag_17_property() public returns (bool) {
    return echidna_flag_17;
  }
  function echidna_flag_18_property() public returns (bool) {
    return echidna_flag_18;
  }
  function echidna_flag_19_property() public returns (bool) {
    return echidna_flag_19;
  }
  function echidna_flag_20_property() public returns (bool) {
    return echidna_flag_20;
  }
  function echidna_flag_21_property() public returns (bool) {
    return echidna_flag_21;
  }
  function echidna_flag_22_property() public returns (bool) {
    return echidna_flag_22;
  }
  function echidna_flag_23_property() public returns (bool) {
    return echidna_flag_23;
  }
  function echidna_flag_24_property() public returns (bool) {
    return echidna_flag_24;
  }
  function echidna_flag_25_property() public returns (bool) {
    return echidna_flag_25;
  }
  function echidna_flag_26_property() public returns (bool) {
    return echidna_flag_26;
  }
  function echidna_flag_27_property() public returns (bool) {
    return echidna_flag_27;
  }
  function echidna_flag_28_property() public returns (bool) {
    return echidna_flag_28;
  }
  function echidna_flag_29_property() public returns (bool) {
    return echidna_flag_29;
  }
  function echidna_flag_30_property() public returns (bool) {
    return echidna_flag_30;
  }
  function echidna_flag_31_property() public returns (bool) {
    return echidna_flag_31;
  }
  function echidna_flag_32_property() public returns (bool) {
    return echidna_flag_32;
  }
  function echidna_flag_33_property() public returns (bool) {
    return echidna_flag_33;
  }
  function echidna_flag_34_property() public returns (bool) {
    return echidna_flag_34;
  }
  function echidna_flag_35_property() public returns (bool) {
    return echidna_flag_35;
  }
  function echidna_flag_36_property() public returns (bool) {
    return echidna_flag_36;
  }
  function echidna_flag_37_property() public returns (bool) {
    return echidna_flag_37;
  }
  function echidna_flag_38_property() public returns (bool) {
    return echidna_flag_38;
  }
  function echidna_flag_39_property() public returns (bool) {
    return echidna_flag_39;
  }
  function echidna_flag_40_property() public returns (bool) {
    return echidna_flag_40;
  }
  function echidna_flag_41_property() public returns (bool) {
    return echidna_flag_41;
  }
  function echidna_flag_42_property() public returns (bool) {
    return echidna_flag_42;
  }
  function echidna_flag_43_property() public returns (bool) {
    return echidna_flag_43;
  }
  function echidna_flag_44_property() public returns (bool) {
    return echidna_flag_44;
  }
  function echidna_flag_45_property() public returns (bool) {
    return echidna_flag_45;
  }
  function echidna_flag_46_property() public returns (bool) {
    return echidna_flag_46;
  }
  function echidna_flag_47_property() public returns (bool) {
    return echidna_flag_47;
  }
}