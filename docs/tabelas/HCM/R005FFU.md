# R005FFU

## Descrição

Ficha Funcional

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| IniOco | Date | Não | Início Ocorrência |
| FimOco | Date | Sim | Fim Ocorrência |
| TipOco | Number(003,0) | Sim | Tipo de Ocorrência para Ficha Funcional |
| CodPrv | Number(003,0) | Sim | Código da Providência |
| CodPun | Number(003,0) | Sim | Código da Punição |
| CodOcE | Number(003,0) | Sim | Ocorrência na Escala |
| DesOco | String(2500) | Sim | Descrição da Anotação da Ficha |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- IniOco

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R005FFU_005

**Tabela:** R005TOC

| Origem | Destino |
|--------|---------|
| TipOco | TipOco |

