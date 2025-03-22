{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
    systems.url = "github:nix-systems/default";
  };
  outputs =
    inputs@{
      flake-parts,
      systems,
      ...
    }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = import systems;
      perSystem =
        { pkgs, lib, ... }:
        {
          packages.buf-generate = pkgs.writeShellApplication {
            name = "buf-generate";
            text = ''
              rm -rf src/arg_services src/google
              ${lib.getExe pkgs.buf} generate
              find src/* -type d -exec touch {}/__init__.py \;
            '';
          };
          devShells.default = pkgs.mkShell {
            packages = with pkgs; [
              uv
              buf
            ];
            shellHook = ''
              uv sync --all-extras --locked
            '';
          };
        };
    };
}
