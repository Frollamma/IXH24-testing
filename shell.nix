{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python3
    pkgs.poetry
  ];

  shellHook = ''
    echo "Welcome to the development shell!"
  '';
}
