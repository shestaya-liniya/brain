# Sketchybar

[Github](https://github.com/FelixKratz/SketchyBar)  
[Nice tutorial](https://www.youtube.com/watch?v=8W06wMNZmo8&t=14s)

Custom menu bar for MacOS

> [!INFO]
> You can find the whole sketchybar config in this repo:
> https://github.com/shestaya-liniya/sketchybar-config

## Left

![](/sketchybar-left.png)

These are [aerospace workspaces](/mac-os-config/aerospace)

::: info  
To connect aerospace with sketchybar you should add this in your `~/.aerospace.toml`.
For more info visit:  
https://nikitabobko.github.io/AeroSpace/goodness#show-aerospace-workspaces-in-sketchybar

```toml
after-startup-command = ['exec-and-forget sketchybar']
exec-on-workspace-change = [
  '/bin/bash', '-c',
  'sketchybar --trigger aerospace_workspace_change FOCUSED_WORKSPACE=$AEROSPACE_FOCUSED_WORKSPACE'
]
```

:::

## Right

![](/sketchybar-right.png)

Most useful info for me to keep it simple

## Full layout

> [!INFO]
> You can still access the default menu bar by hovering the top
> <video controls="controls" src="/sketchybar-default-menu.mp4" />

![](/vscode-layout.png)
