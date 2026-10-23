# R034WIN

## Descrição

Comprovante de Informe de Rendimentos em PDF

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
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| AnoRen | Date | Não | Ano Rendimentos |
| DocIRF | Image | Sim | Documento |
| NomArq | String(250) | Sim | Nome Arquivo |
| DatHor | Number(014,6) | Sim | Data e Hora de geração |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- AnoRen

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034WIN_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

