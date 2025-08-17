# 源文件目录
SRC_DIR := src

# 输出目录
OUT_DIR := build

# 查找所有 .xy 文件
XY_FILES := $(shell find $(SRC_DIR) -name "*.xy")

# 对应的输出 .py 文件
PY_FILES := $(patsubst $(SRC_DIR)/%.xy,$(OUT_DIR)/%.py,$(XY_FILES))

# 默认目标
all: $(PY_FILES)

# 规则：将 .xy 编译为 .py，并隐藏命令本身
$(OUT_DIR)/%.py: $(SRC_DIR)/%.xy
	@mkdir -p $(dir $@)
	@echo -e '\033[32mxiaoyi\033[0m: "$<" \033[32m➔ \033[0m "$@"'

	@xiaoyi "$<" "$@"

# 清理生成文件
clean:
	rm -rf $(OUT_DIR)
