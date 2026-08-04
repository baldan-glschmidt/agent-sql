# E725CRS

## Descrição

Ficha - Roteiro - Cadastro Centro de Recursos Substitutos

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodCre | String(008) | Não | Código do Centro de Recurso Titular |
| CreSbs | String(008) | Não | Código do Centro de Recurso Substituto |
| PerEqi | Number(005,2) | Sim | Percentual de equivalência do Substituto em relação ao Titular |
| TipCrs | String(001) | Sim | Define a finalidade do recurso substituto e onde o mesmo será utilizado |
| AltSbs | String(001) | Sim | Indica se o Recurso é Substituto (Sapiens) ou Alternativo (Escalonador) |

---

## Chave Primária

- CodEmp
- CodCre
- CreSbs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E725CRS_001

**Tabela:** E725CRE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCre | CodCre |

### IR_E725CRS_002

**Tabela:** E725CRE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CreSbs | CodCre |

