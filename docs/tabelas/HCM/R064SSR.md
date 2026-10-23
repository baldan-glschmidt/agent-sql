# R064SSR

## Descrição

Substituição de Serviço

---

## Resumo

- Campos: 9
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
| DatIni | Date | Não | Data Inicial da Substituição |
| DatFim | Date | Sim | Data Final da Substituição |
| EmpSub | Number(004,0) | Sim | Código da Empresa do Substituto |
| TClSub | Number(001,0) | Sim | Tipo de Colaborador Substituto |
| CadSub | Number(009,0) | Sim | Cadastro do Substituto |
| CodOcE | Number(003,0) | Sim | Ocorrência na Escala |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R064SSR_008

**Tabela:** R005OCE

| Origem | Destino |
|--------|---------|
| CodOcE | CodOcE |

