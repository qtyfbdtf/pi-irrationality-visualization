from manim import *
import numpy as np


class TwoRotatingRods(Scene):
    def construct(self):
        # Parameters
        inner_rotation_speed = 5  # Speed of the inner rod (theta)
        outer_rotation_speed = PI  # Speed of the outer rod (pi * theta)
        rod_length = 2  # Length of both rods (2 is recommended)
        trace_thickness = 1  # Thickness of the trace path
        total_time = 10  # Duration of the animation in seconds

        # Create objects
        origin = Dot(ORIGIN, color=WHITE)  # Fixed point
        inner_rod = Line(ORIGIN, RIGHT * rod_length, color=WHITE)  # Thicker inner rod
        outer_rod = Line(RIGHT * rod_length, RIGHT * 2 * rod_length, color=WHITE)  # Thicker outer rod

        # Initialize trace path
        trace_path = VMobject(color=YELLOW, stroke_width=trace_thickness)  # Set trace thickness
        trace_path.set_points_as_corners([outer_rod.get_end(), outer_rod.get_end()])

        # Add objects to the scene
        self.add(origin, inner_rod, outer_rod, trace_path)

        # Track elapsed time
        elapsed_time = [0]

        # Animation logic
        def update_objects(mob, dt):
            elapsed_time[0] += dt  # Update elapsed time

            # Update rotation angles
            theta_inner = inner_rotation_speed * elapsed_time[0]
            theta_outer = outer_rotation_speed * elapsed_time[0]

            # Calculate new positions
            new_inner_end = (
                RIGHT * rod_length * np.cos(theta_inner) +
                UP * rod_length * np.sin(theta_inner)
            )
            new_outer_end = (
                new_inner_end +
                RIGHT * rod_length * np.cos(theta_outer) +
                UP * rod_length * np.sin(theta_outer)
            )

            # Update rods positions
            inner_rod.put_start_and_end_on(ORIGIN, new_inner_end)
            outer_rod.put_start_and_end_on(new_inner_end, new_outer_end)

            # Redraw the rods explicitly
            self.remove(inner_rod, outer_rod)  # Remove old rods
            self.add(inner_rod, outer_rod)  # Add updated rods

            # Update trace path (mob is trace_path)
            mob.add_points_as_corners([new_outer_end])

        # Add updater to trace path to control the entire animation
        trace_path.add_updater(update_objects)

        # Run the animation
        self.wait(total_time)

        # Remove updater to finalize the animation
        trace_path.clear_updaters()
