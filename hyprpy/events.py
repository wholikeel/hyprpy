"""Hyprland Events
See [Hyprland events list](https://wiki.hyprland.org/IPC/#events-list)
"""

from dataclasses import dataclass


@dataclass
class Workspace:
    """Emitted on workspace change.

    Is emitted ONLY when a user requests a workspace change,
    and is not emitted on mouse movements (see activemon)
    """

    workspace_name: str


@dataclass
class WorkspaceV2:
    """Emitted on workspace change.

    Is emitted ONLY when a user requests a workspace change,
    and is not emitted on mouse movements (see activemon)
    """

    workspace_id: int
    workspace_name: str


@dataclass
class FocusedMonitor:
    """Emitted on the active monitor being changed."""

    monitor_name: str
    workspace_name: str


@dataclass
class ActiveWindow:
    """Emitted on the active window being changed."""

    window_class: str
    window_title: str


@dataclass
class ActiveWindowV2:
    """Emitted on the active window being changed."""

    window_address: str


@dataclass
class Fullscreen:
    """Emitted when a fullscreen status of a window changes.

    A fullscreen event is not guaranteed to fire on/off once in succession.
    
    Some windows may fire multiple requests to be fullscreened, resulting in
    multiple fullscreen events.
    """

    fullscreen_state: bool


@dataclass
class MonitorRemoved:
    """Emitted when a monitor is removed (disconnected)"""

    monitor_name: str


@dataclass
class MonitorAdded:
    """Emitted when a monitor is added (connected)"""

    monitor_name: str


@dataclass
class MonitorAddedV2:
    """Emitted when a monitor is added (connected)"""

    monitor_id: int
    monitor_name: str
    monitor_description: str


@dataclass
class CreateWorkspace:
    """Emitted when a workspace is created"""

    workspace_name: str


@dataclass
class CreateWorkspaceV2:
    """Emitted when a workspace is created"""

    workspace_id: int
    workspace_name: str


@dataclass
class DestroyWorkspace:
    """Emitted when a workspace is destroyed"""

    workspace_name: str


@dataclass
class DestroyWorkspaceV2:
    """Emitted when a workspace is destroyed"""

    workspace_id: int
    workspace_name: str


@dataclass
class MoveWorkspace:
    """Emitted when a workspace is moved to a different monitor"""

    workspace_name: str
    monitor_name: str


@dataclass
class MoveWorkspaceV2:
    """Emitted when a workspace is moved to a different monitor"""

    workspace_id: int
    workspace_name: str
    monitor_name: str


@dataclass
class RenameWorkspace:
    """Emitted when a workspace is renamed"""

    workspace_id: int
    workspace_new_name: str


@dataclass
class ActiveSpecial:
    """Emitted when the special workspace opened in a monitor changes

    Closing results in an empty WORKSPACENAME.
    """

    workspace_name: str
    monitor_name: str


@dataclass
class ActiveLayout:
    """Emitted on a layout change of the active keyboard"""

    keyboard_name: str
    layout_name: str


@dataclass
class OpenWindow:
    """Emitted when a window is opened"""

    window_address: str
    workspace_name: str
    window_class: str
    window_title: str


@dataclass
class CloseWindow:
    """Emitted when a window is closed"""

    window_address: str


@dataclass
class MoveWindow:
    """Emitted when a window is moved to a workspace"""

    window_address: str
    workspace_name: str


@dataclass
class MoveWindowV2:
    """Emitted when a window is moved to a workspace"""

    window_address: str
    workspace_id: int
    workspace_name: str


@dataclass
class OpenLayer:
    """Emitted when a layerSurface is mapped"""

    namespace: str


@dataclass
class CloseLayer:
    """Emitted when a layerSurface is unmapped"""

    namespace: str


@dataclass
class Submap:
    """Emitted when a keybind submap changes. Empty means default."""

    submap_name: str


@dataclass
class ChangeFloatingMode:
    """Emitted when a window changes its floating mode. FLOATING is either 0 or 1."""

    window_address: str
    floating: bool


@dataclass
class Urgent:
    """Emitted when a window requests an urgent state"""

    window_address: str


@dataclass
class Minimize:
    """Emitted when a window requests a change to its minimized state.

    MINIMIZED is either 0 or 1.
    """

    window_address: str
    window_minimized: bool


@dataclass
class ScreenCast:
    """Emitted when a screencopy state of a client changes.

    Keep in mind there might be multiple separate clients.
    State is 0/1, owner is 0 - monitor share, 1 - window share
    """

    screencopy_state: bool
    window_owner: bool


@dataclass
class WindowTitle:
    """Emitted when a window title changes."""

    window_address: str


@dataclass
class WindowTitleV2:
    """Emitted when a window title changes."""

    window_address: str
    window_title: str


@dataclass
class ToggleGroup:
    """Emitted when togglegroup command is used.

    Returns `state,handle` where the state is a toggle status and the handle
    is one or more window addresses separated by a comma

    e.g. 0,0x64cea2525760,0x64cea2522380 where 0 means that a group has been
    destroyed and the rest informs which windows were part of it.
    """

    toggle_status: bool
    window_addresses: list[str]


@dataclass
class MoveIntoGroup:
    """Emitted when the window is merged into a group.

    Returns the address of a merged window.
    """

    window_address: str


@dataclass
class MoveOutOfGroup:
    """Emitted when the window is removed from a group.

    Returns the address of a removed window.
    """

    window_address: str


@dataclass
class IgnoreGroupLock:
    """Emitted when ignoregrouplock is toggled."""

    ignore_state: bool



@dataclass
class LockGroups:
    """Emitted when lockgroups is toggled."""

    lock_state: bool



@dataclass
class ConfigReloaded:
    """Emitted when the config is done reloading"""


@dataclass
class Pin:
    """Emitted when a window is pinned or unpinned."""

    window_address: str
    pinned: bool



type WorkspaceEvent = (
    Workspace
    | WorkspaceV2
    | CreateWorkspace
    | CreateWorkspaceV2
    | DestroyWorkspace
    | DestroyWorkspaceV2
    | MoveWorkspace
    | MoveWorkspaceV2
    | RenameWorkspace
    | ActiveSpecial
)

type WindowEvent = (
    ActiveWindow
    | ActiveWindowV2
    | OpenWindow
    | CloseWindow
    | MoveWindow
    | MoveWindowV2
    | Fullscreen
    | ChangeFloatingMode
    | Minimize
    | Pin
    | Urgent
)

type MonitorEvent = (
    MonitorRemoved
    | MonitorAdded
    | MonitorAddedV2
    | WindowTitle
    | WindowTitleV2
    | FocusedMonitor
)

type LayerEvent = OpenLayer | CloseLayer | CloseLayer

type GroupEvent = (
    ToggleGroup | MoveIntoGroup | MoveOutOfGroup | IgnoreGroupLock | LockGroups
)

type MiscEvent = ActiveLayout | Submap | ScreenCast | ConfigReloaded

type HyprlandEvent = (
    WorkspaceEvent | MonitorEvent | WindowEvent | LayerEvent | GroupEvent | MiscEvent
)
