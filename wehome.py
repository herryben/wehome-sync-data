#-*- coding: utf-8 -*-
'''
This file is the main enter for the project
'''
# import sys
import importlib
import click as cli
 
@cli.command()
@cli.option('--project', prompt='enter project name',
  type=str, help='project to sync data')
def sync(project):
  try:
    command = 'job.{project}.{project}'.format(project=project)
    project = importlib.import_module(command)
    project.sync()
  except ImportError:
    print "Project don't exists"

if __name__ == '__main__':
  sync()
