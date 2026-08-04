# E710VRO

## Descrição

Ficha - Roteiro - Versões Roteiro

---

## Resumo

- Campos: 11
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodRot | String(014) | Não | Código do Roteiro de Produção associado ao Produto |
| DatAlt | Date | Não | Data de Alteração para geração de versões p/ custos |
| LotTec | Number(010,3) | Não | Quantidade do Lote Técnico ideal, para a fabricação do Produto |
| QtdBas | Number(014,5) | Não | Quantidade Base em relação aos tempos informados |
| TmpObt | Number(008,2) | Não | Tempo de Produção, em dias, proporcional ao lote técnico a produzir |
| TmpFix | Number(008,2) | Não | Tempo Fixo em Dias |
| DatGer | Date | Não | Data de geração da versão |
| VerRot | String(015) | Sim | Última versão do roteiro na qual é incrementada em cada nova alteração |
| CodUsu | Number(010,0) | Sim | Código do Usuário que alterou o registro |
| HorGer | Number(005,0) | Sim | Hora da geração da versão |

---

## Chave Primária

- CodEmp
- CodRot
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
