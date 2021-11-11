{ pkgs ? import <nixpkgs> {} }:

let
  my-python = pkgs.python38;
  python-with-my-packages = my-python.withPackages (p: with p; [
    numpy
  ]);
in
pkgs.mkShell {
  buildInputs = [
    python-with-my-packages
  ];
}