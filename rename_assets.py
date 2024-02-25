import unreal

def rename_assets(search_pattern, replaced_pattern, use_case):
    # unreal classes
    system_lib = unreal.SystemLibrary()
    editor_util = unreal.EditorUtilityLibrary()
    string_lib = unreal.StringLibrary()

    # 選択したアセットの取得
    selected_assets = editor_util.get_selected_assets()
    num_assets = len(selected_assets)
    replaced = 0

    unreal.log("Selected {} asset/s".format(num_assets))

    for asset in selected_assets:
        asset_name = system_lib.get_object_name(asset)

        # 変更対象のアセット名が含まれているかを確認
        if string_lib.contains(asset_name, search_pattern, use_case = use_case):
            search_case = unreal.SearchCase.CASE_SENSITIVE if use_case else unreal.SearchCase.IGNORE_CASE
            replaced_name = string_lib.replace(asset_name, search_pattern, replaced_pattern, search_case=search_case)
            editor_util.rename_asset(asset, replaced_name)

            replaced += 1
            unreal.log("Replaced {} with {}".format(asset_name, replaced_name))

        else:
            unreal.log("{} did not match the search pattern, was skiooed".format(asset_name))

    unreal.log("Replaced {} of {} assets".format(replaced, num_assets))

# アセットの変更前の名前と変更後の名前
rename_assets("New", "Old", False)