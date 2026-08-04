# E700IBN

## Descrição

Ficha - Modelo - Itens Combinações de Componentes

---

## Resumo

- Campos: 12
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Empresa |
| CodMod | String(014) | Não | Código do Modelo associado ao Produto |
| CodCbn | Number(006,0) | Não | Código da combinação, gerado automaticamente ao combinar componentes do modelo |
| SeqCbn | Number(004,0) | Não | Número  Sequencial  das combinações |
| CodCmp | String(014) | Não | Código do Componente (Produto) |
| DerCmp | String(007) | Sim | Derivação do Componente FIXA (p/ todos os Produtos compostos que estão associados) |
| CodEtg | Number(004,0) | Sim | Código do Estágio de Produção onde  o componente é agregado ao Produto composto |
| SeqMod | Number(004,0) | Sim | Sequência lógica onde o Componente é utilizado na fabricação do Produto composto |
| VisCbn | String(001) | Sim | Visualizar componente na árvore de combinaçôes |
| CodUsu | Number(010,0) | Não | Código do Usuário que alterou |
| DatGer | Date | Não | Data Geração ou Alteração da ligação |
| HorGer | Number(005,0) | Não | Hora da geração/última alteração do registro |

---

## Chave Primária

- CodEmp
- CodMod
- CodCbn
- SeqCbn

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E700IBN_001

**Tabela:** E700MOD

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMod | CodMod |

