cmake_minimum_required(VERSION 4.1)

function(SHIT_subscribe target_name template_path output_path)
    find_package(Python3 COMPONENTS Interpreter REQUIRED)

    add_custom_command(
            OUTPUT ${output_path}
            COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_FUNCTION_LIST_DIR}/main.py -t=${CMAKE_CURRENT_SOURCE_DIR}/${template_path} -i=${target_name} > ${output_path}
            DEPENDS ${CMAKE_CURRENT_FUNCTION_LIST_DIR}/main.py
            WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
            VERBATIM
    )

    add_custom_target(${target_name}_SHITTER ALL DEPENDS ${output_path})

    target_include_directories(${target_name} PUBLIC ${CMAKE_CURRENT_BINARY_DIR})
    add_dependencies(${target_name} ${target_name}_SHITTER)

    message(STATUS "SHIT configured to ${CMAKE_CURRENT_BINARY_DIR}/${output_path}")
endfunction()