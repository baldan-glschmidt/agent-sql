# E710VCT

## Descrição

Ficha - Roteiro - Versões Estágios

---

## Resumo

- Campos: 17
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodRot | String(014) | Não | Código do Roteiro de Produção |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção agregado ao Roteiro |
| SfxEtr | Number(003,0) | Não | Sufixo do Estágio (1=Padrão, 2-999=Alternativas) |
| DatAlt | Date | Não | Data da alteração |
| TmpFix | Number(008,2) | Sim | Quantidade de Dias (preparação, espera, etc.) gasto no Estágio  independente da quantidade a produzir |
| TipPos | Number(001,0) | Não | Tipo Posicionamento (1=Inicia após fim do anterior, 2=inicia junto, 3=finaliza junto) |
| CodSer | String(014) | Sim | Código do Serviço (Quando Estágio é realizado por Terceiros) |
| CodFor | Number(009,0) | Sim | Código Fornecedor do Serviço (Quando Estágio é realizado por Terceiros) |
| FilPro | Number(005,0) | Sim | Filial de Produção do Estágio |
| CodCel | String(004) | Sim | Código da Célula de Produção (Grupos de Trabalho) |
| CodCcu | String(009) | Sim | Código do Centro de Custos |
| DatGer | Date | Sim | Data geração de versão |
| LotTec | Number(010,3) | Sim | Lote Técnico ideal, de fabricação a nível de Estágio |
| VerRot | String(015) | Sim | Última versão do roteiro na qual é incrementada em cada nova alteração |
| CodUsu | Number(010,0) | Sim | Código do usuário que alterou o registro |
| HorGer | Number(005,0) | Sim | Hora da geração da versão |

---

## Chave Primária

- CodEmp
- CodRot
- CodEtg
- SfxEtr
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E710VCT_001

**Tabela:** E710ROT

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodRot | CodRot |

### IR_E710VCT_002

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

