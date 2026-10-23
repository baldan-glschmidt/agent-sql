# R044SIN

## Descrição

Dissídio - Sindicatos

---

## Resumo

- Campos: 16
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| CodSin | Number(004,0) | Não | Código do Sindicato |
| DatDis | Date | Sim | Data Homologação do Dissídio |
| TipAco | Number(001,0) | Sim | Tipo de Acordo |
| CodPro | Number(011,0) | Sim | Código do Processo |
| AnoPro | Number(004,0) | Sim | Ano do Processo |
| NumJcj | Number(005,0) | Sim | Número da Vara/JCJ |
| IniPro | Date | Sim | Início do Processo |
| FimPro | Date | Sim | Fim do Processo |
| CmpDis | Date | Sim | Competência do Dissídio |
| DatEft | Date | Sim | Data Início do Efeito do Dissídio |
| ObsDis | String(255) | Sim | Observação do Dissídio |
| DatLei | Date | Sim | Data da Lei que determinou o reajuste retroativo |
| NumLei | String(012) | Sim | Número da Lei que determinou o reajuste retroativo |
| EftLei | Date | Sim | Data de Início do Efeito da Lei que determinou o reajuste retroativo |

---

## Chave Primária

- NumEmp
- CodCal
- CodSin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
