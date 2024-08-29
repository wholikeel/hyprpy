{ lib
, python312Packages
 }:

python312Packages.buildPythonPackage rec {
  pname = "hyprpy";
  version = "0.0.1";
  pyproject = true;

  src = ./.;

  postPatch = ''
  '';

  build-system = [
  ];

  dependencies = [
    python312Packages.setuptools
  ];

  nativeCheckInputs = [
  ];

  meta = {
    changelog = "";
    description = "Hyprland API wrapper";
    homepage = "";
    license = lib.licenses.mit;
    maintainers = with lib.maintainers; [];
  };
}
