# E700VCC

## Descrição

Ficha - Modelo - Versões Consumos

---

## Resumo

- Campos: 17
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodMod | String(014) | Não | Código do Modelo associado ao Produto |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção onde o Componente é agregado ao Produto composto |
| SeqMod | Number(004,0) | Não | Sequência lógica onde o Componente é utilizado na fabricação do Produto composto |
| CodDer | String(007) | Não | Derivação associada ao Modelo |
| DatAlt | Date | Não | Data de Alteração do componente válido p/ Custos |
| VerMod | String(015) | Não | Última versão do Modelo na qual e incrementada em cada nova alteração |
| CodCmp | String(014) | Sim | Código do Componente(Produto) |
| DerCmp | String(007) | Sim | Derivação do Componente FIXA (p/ todos os Produtos compostos que estão associados) |
| QtdUti | Number(014,5) | Não | Quantidade utilizada do componente (Proporcional/Fixa) |
| QtdFrq | Number(014,5) | Sim | Quantidade Frequencial (Produto produzido) que o componente é consumido (apropriado) |
| PrdQtd | Number(014,5) | Sim | Quantidade de perda do componente no processo de fabricação |
| PerPrd | Number(006,3) | Sim | % perda do componente no processo de fabricação |
| UniMe2 | String(003) | Não | Unidade de medida  do componente na Produção |
| DatGer | Date | Sim | Data da geração da versão |
| CodUsu | Number(010,0) | Sim | Código do usuário que alterou o registro |
| HorGer | Number(005,0) | Sim | Hora da geração da versão |

---

## Chave Primária

- CodEmp
- CodMod
- CodEtg
- SeqMod
- CodDer
- DatAlt
- VerMod

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E700VCC_013

**Tabela:** E015MED

| Origem | Destino |
|--------|---------|
| UniMe2 | UniMed |

