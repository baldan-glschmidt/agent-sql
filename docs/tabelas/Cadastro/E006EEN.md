# E006EEN

## Descrição

Tabelas - Estrutura de Endereços

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEen | String(018) | Não | Código do endereço |
| DesEen | String(100) | Não | Descrição do endereço |
| MskEen | String(018) | Não | Máscara do endereço |
| NivEen | Number(002,0) | Não | Nível da máscara do endereço |
| CodPai | String(004) | Sim | Código do país referente ao endereço |
| SigUfs | String(002) | Sim | Sigla do estado referente ao endereço |
| IndCid | String(001) | Sim | Indicativo se a cidade é definida por esse nível da estrutura |
| CepIni | Number(008,0) | Sim | CEP inicial da cidade referente ao endereço |

---

## Chave Primária

- CodEen

---

## Índices

### E006EENIndice2

**Tipo:** Unico

Campos:
- MskEen

---

## Relacionamentos

Nenhum relacionamento cadastrado.
