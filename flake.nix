{
  description = "A flake for Python3 and Poetry";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }: {
    defaultPackage.x86_64-linux = nixpkgs.lib.mkShell {
      buildInputs = [
        nixpkgs.python3
        nixpkgs.poetry
      ];
    };
  };
}
