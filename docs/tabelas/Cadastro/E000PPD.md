# E000PPD

## Descrição

Integrações - Estoques - Posição de estoque do produto em determinado momento

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IDEUNI | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação |
| CodDep | String(010) | Não | Código do depósito |
| QtdEst | Number(014,5) | Sim | Quantidade física total do estoque no depósito no momento da geração do estoque |
| TemEst | Number(001,0) | Sim | Indicativo se o item tem estoque |
| UsuGer | Number(010,0) | Não | Usuário responsável pela geração do registro |
| DatGer | Date | Não | Data da geração do registro |
| HorGer | Number(005,0) | Não | Hora da geração do registro |

---

## Chave Primária

- IDEUNI

---

## Índices

### E000EPDINDICE1

**Tipo:** Unico

Campos:
- CodEmp
- CodPro
- CodDer
- CodDep

---

## Relacionamentos

Nenhum relacionamento cadastrado.
