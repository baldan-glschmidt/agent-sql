# R014MHE

## Descrição

Parâmetros p/ Média de Horas Extras (Obsoleta)

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(004,0) | Não | Código do Sindicato |
| TipMed | Number(001,0) | Não | Tipo da Média |
| ForCal | Number(002,0) | Não | Forma de Cálculo da Média de Horas Extras |
| MesPes | Number(002,0) | Sim | Quantidade de Meses a pesquisar p/ média |
| MesMed | Number(002,0) | Sim | Quantidade de "maiores meses" a utilizar na média |
| MesDiv | Number(002,0) | Sim | Qtde de meses que se dividirá a soma dos valores apurados |

---

## Chave Primária

- CodSin
- TipMed
- ForCal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R014MHE_000

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

