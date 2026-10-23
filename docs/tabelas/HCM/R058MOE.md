# R058MOE

## Descrição

Modelos por Empresa

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ModRlg | Number(004,0) | Não | Código do Modelo do Coletor |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| DirMar | String(200) | Sim | Diretório dos Arquivos de Marcações do Coletor |
| DirRej | String(200) | Sim | Diretório dos Arquivos das Marcações Rejeitadas |
| MesCol | String(035) | Sim | Registro Mestre dos Arquivos de Marcações do Coletor |
| MarCol | String(100) | Sim | Registro de Marcação dos Arquivos de Marcações do Coletor |

---

## Chave Primária

- ModRlg
- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058MOE_000

**Tabela:** R058MOD

| Origem | Destino |
|--------|---------|
| ModRlg | ModRlg |

