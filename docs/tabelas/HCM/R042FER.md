# R042FER

## Descrição

HomologNet - Períodos de Férias

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| IniPer | Date | Não | Data Início do Período |
| FimPer | Date | Sim | Data Fim do Período |
| FalPer | Number(003,0) | Sim | Faltas Injustificadas no Período |
| SitPer | Number(001,0) | Sim | Quitação Férias |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- IniPer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R042FER_002

**Tabela:** R042COL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

