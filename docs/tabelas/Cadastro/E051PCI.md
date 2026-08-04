# E051PCI

## Descrição

Cadastro do Crédito Presumido da CBS/IBS

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPci | String(003) | Não | Código Interno |
| CodStr | String(002) | Não | Código da classificação do crédito presumido |
| DesStr | String(255) | Sim | Descrição da classificação do crédito presumido |
| TipApl | String(003) | Não | Tipo de aplicação do crédito presumido |
| PerPci | Number(008,4) | Não | Percentual do crédito presumido |
| ConSus | String(001) | Não | Crédito presumido em condição suspensiva |
| DedCre | String(001) | Sim | Deduz o valor do crédito presumido do valor total |

---

## Chave Primária

- CodPci

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
