# E075OBS

## Descrição

Cadastros - Produtos - Observações Adicionais do Produto/Derivação

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Derivação do  produto |
| DatGer | Date | Não | Data de geração da observação |
| SeqObs | Number(004,0) | Não | Sequência numérica do histórico do produto |
| TipObs | String(001) | Não | Tipo da observação |
| DesObs | String(240) | Não | Histórico do produto - informativos e/ou detalhes técnicos |
| HorAtu | Number(005,0) | Sim | Hora da atualização do registro |
| CodUsu | Number(010,0) | Não | Código do usuário que atualizou  o registro |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- DatGer
- SeqObs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E075OBS_001

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

