# R034FAP

## Descrição

Faixa de Acesso da Permissão do Colaborador

---

## Resumo

- Campos: 12
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdtPes | String(023) | Não | Identificador da Pessoa |
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor |
| VerPlf | Number(003,0) | Não | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Não | Código do Local Físico |
| IniFai | Number(005,0) | Não | Início da Faixa p/ Marcação de Acesso |
| DiaSem | Number(001,0) | Não | Dia da Semana |
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| NumAmb | Number(009,0) | Sim | Ambiente da Planta |
| FimFai | Number(005,0) | Sim | Fim da Faixa p/ Marcação de Acesso |
| EstPos | Number(003,0) | Sim | Código da Estrutura de Postos de Trabalho |
| PosTra | String(024) | Sim | Código do Posto de Trabalho |

---

## Chave Primária

- IdtPes
- VerPlf
- CodPlf
- CodPlt
- CodRlg
- DiaSem
- IniFai
- CodDsp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
