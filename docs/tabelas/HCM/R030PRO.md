# R030PRO

## Descrição

Processos Judiciais

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodPro | Number(009,0) | Não | Número do Processo/Benefício |
| NumPro | String(021) | Sim | Número do Processo/Benefício |
| TipPJu | Number(001,0) | Sim | Tipo do Processo |
| ExtINS | Number(001,0) | Sim | Extensão Prev. Social |
| ClaPro | Number(003,0) | Sim | Classificação do Processo |
| BasDes | Number(001,0) | Sim | Informar se o processo deve ser enviado ao eSocial por esta Empresa |
| ObsPro | String(255) | Sim | Observação |

---

## Chave Primária

- NumEmp
- CodPro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
