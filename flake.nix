{
  description = "Hyprpy - Typed Hyprland API wrapped";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/24.05";
    nixpkgs-unstable.url = "github:NixOS/nixpkgs/nixos-unstable";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    nixpkgs,
    nixpkgs-unstable,
    utils,
    ...
  }:
    utils.lib.eachDefaultSystem
    (system: let
      pkgs = nixpkgs.legacyPackages.${system};
      unstable-pkgs = nixpkgs-unstable.legacyPackages.${system};

      pythonWithPackages = pkgs.python312.withPackages (ps: with ps; [
        setuptools
        wheel
        build
        ]);
    in {
      packages = {
        default = pkgs.callPackage ./default.nix { };
      };
      apps = {
      };
      devShells = {
        default = pkgs.mkShell {
          name = "hyprpr-devshell";
          packages = [
            unstable-pkgs.basedpyright
            unstable-pkgs.ruff
            pythonWithPackages
          ];
        };
      };
    });
}


