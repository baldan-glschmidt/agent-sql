# E700VMO

## Descrição

Ficha - Modelo - Versões Modelo

---

## Resumo

- Campos: 19
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa. |
| CodMod | String(014) | Não | Código do Modelo associado ao Produto. |
| DatAlt | Date | Não | Data da alteração para geração de versões p/ custos |
| VerMod | String(015) | Não | Última versão do modelo na qual é incrementada em cada nova alteração |
| QtdBas | Number(014,5) | Sim | Quantidade base p/ compor proporcionalmente o consumo dos componentes |
| CodClc | String(010) | Sim | Código da coleção do produto |
| CodClf | String(003) | Sim | Código interno da classificação fiscal do produto |
| FilPrd | Number(005,0) | Sim | Código da filial de produção do produto |
| QtdMax | Number(012,5) | Sim | Quantidade máxima para uma ordem produção/compra |
| CodAem | String(010) | Sim | Código do agrupamento para embalagens |
| CodAge | String(005) | Sim | Código de agrupamento de materiais/produtos para estoques |
| TolQmx | Number(005,3) | Sim | Tolerância da quantidade máxima defininida no produto |
| CodRot | String(014) | Sim | Código do roteiro de produção p/ produto fabricado |
| DatGer | Date | Não | Data de geração da versão |
| CodUsu | Number(010,0) | Sim | Código do usuário que alterou o registro |
| HorGer | Number(005,0) | Sim | Hora da geração da versão |
| CodCre | String(008) | Não | Código do Centro de Recurso (conjunto Máquina/Pessoa c/ mesma capacidade produtiva) |
| VolCre | Number(011,5) | Sim | Volume do recurso |
| FenCre | Number(011,5) | Sim | Fator de enchimento do recurso |

---

## Chave Primária

- CodEmp
- CodMod
- DatAlt
- VerMod

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
