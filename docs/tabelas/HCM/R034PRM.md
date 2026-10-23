# R034PRM

## Descrição

Permissão de Acesso por Colaborador

---

## Resumo

- Campos: 14
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdtPes | String(023) | Não | Identificador da Pessoa |
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor |
| VerPlf | Number(003,0) | Não | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Não | Código do Local Físico |
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| NumAmb | Number(009,0) | Sim | Ambiente da Planta |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| SeqReg | Number(015,0) | Sim | Sequencia do Registro |
| EstPos | Number(003,0) | Sim | Código da Estrutura de Postos de trabalho |
| PosTra | String(024) | Sim | Código do Posto de Trabalho |
| OriDef | Number(001,0) | Sim | Origem da Definição |

---

## Chave Primária

- IdtPes
- VerPlf
- CodPlf
- CodPlt
- CodRlg
- CodDsp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034PRM_001

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

